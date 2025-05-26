# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from pokedex_dataset import load_data_pokedex
from recommender import prepare_data, recommend_pokemon

app = FastAPI()

# ✅ Definindo o schema da requisição
class PokemonRequest(BaseModel):
    name: str
    top_n: int = 5

# ✅ Carregando dados e preparando modelo
df_pokedex = load_data_pokedex('pokemon_recommender/data/pokemon.csv')
X, pokemon_names, model, pipeline = prepare_data(df_pokedex)  # ✅

@app.get("/")
def read_root():
    return {"message": "API de Recomendação Pokémon funcionando!"}

@app.post("/recomendar/")
def recomendar(req: PokemonRequest):
    print("Recebida requisição:", req)
    
    name = req.name
    top_n = req.top_n

    if name not in df_pokedex["name"].values:
        print(f"Pokémon '{name}' não encontrado.")
        raise HTTPException(status_code=404, detail=f"Pokémon '{name}' não encontrado.")
    
    print(f"Recomendando para {name} os top {top_n} mais próximos...")

    recommended = recommend_pokemon(name, top_n, df_pokedex, X, pokemon_names, model)

    print("Recomendações geradas:", recommended)
    
    return {"recomendacoes": recommended}

