from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pokedex_dataset import load_data_pokedex
from recommender import prepare_data, recommend_pokemon
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from typing import List
from authentication import router   # <- importa o router de auth.py

app = FastAPI()

#part not used about authentication
app.include_router(router)

# ✅ Definindo o schema da requisição
class PokemonRequest(BaseModel):
    name: str
    top_n: int = 10

class TeamRequest(BaseModel):
    team: List[str]

# ✅ Carregando dados e preparando modelo
df_pokedex = load_data_pokedex('pokemon_dataset/pokemon_recommender/data/pokemon.csv')
df_pokedex["name"] = df_pokedex["name"].str.lower()  # Normalizando os nomes dos Pokémon
X, pokemon_names, model, pipeline = prepare_data(df_pokedex)  # ✅

@app.post("/recommend/")
def recomendar(req: PokemonRequest):
    print('requisition received', req)
    name = req.name.lower()
    top_n = req.top_n

    if name not in df_pokedex["name"].values:
        raise HTTPException(status_code=404, detail=f"Pokémon '{name}' not found.")
    
    recommended = recommend_pokemon(name, top_n, df_pokedex, X, pokemon_names, model)

    return {"recommendation": recommended}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

'''
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Recomendador</title>
        </head>
        <body>
            <h2>Recomendador</h2>
            <form id="form">
                <label for="name">Nome :</label>
                <input type="text" id="name" name="name" required><br><br>

                <label for="top_n">Quantidade de recomendações:</label>
                <input type="number" id="top_n" name="top_n" value="5" required><br><br>

                <button type="submit">Recomendar</button>
            </form>
            <br>
            <div id="result"></div>

            <script>
                document.getElementById('form').addEventListener('submit', async function(e) {
                    e.preventDefault();
                    const name = document.getElementById('name').value;
                    const top_n = parseInt(document.getElementById('top_n').value);

                    const response = await fetch('/recommend/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ name: name, top_n: top_n })
                    });

                    const resultDiv = document.getElementById('result');

                    if (response.ok) {
                        const data = await response.json();
                        resultDiv.innerHTML = "<strong>Recomendações:</strong> " + data.recomendacoes.join(", ");
                    } else {
                        const error = await response.json();
                        resultDiv.innerHTML = "<strong>Erro:</strong> " + error.detail;
                    }
                });
            </script>
        </body>
    </html>
    """
'''
# Configura pasta de arquivos estáticos e templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/team_analysis/")
def analyze_team(req: TeamRequest):
    stats = ['hp', 'attack', 'defense', 'sp.atk', 'sp.def', 'speed']
    filtered = df_pokedex[df_pokedex['name'].isin(req.team)]
    if filtered.empty:
        return {"stats": [0] * len(stats)}
    mean_stats = filtered[stats].mean().tolist()
    return {"stats": mean_stats}




