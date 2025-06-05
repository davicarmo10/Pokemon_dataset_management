# 🔍 Projeto / Project: Pokémon Recommender + Team Analysis

Este projeto é uma aplicação completa que utiliza **FastAPI** no backend e **JavaScript/Chart.js** no frontend, com foco em:
- Recomendação de Pokémon semelhantes
- Análise gráfica dos status médios de um time de até 6 Pokémon

This is a full-stack application using **FastAPI** as backend and **JavaScript/Chart.js** on the frontend, with features like:
- Recommending similar Pokémon
- Visual team analysis of up to 6 Pokémon

---

## ✨ Tecnologias Utilizadas / Technologies Used

| Camada / Layer | Tecnologias / Technologies |
|----------------|-----------------------------|
| Backend        | FastAPI, Pydantic, scikit-learn, pandas |
| Frontend       | HTML, CSS, JavaScript, Chart.js |
| Dados / Data   | CSV file with Pokémon attributes |

---

## 📦 Funcionalidades / Features

### ✅ Recomendação de Pokémon / Pokémon Recommendation
- Envia o nome de um Pokémon e recebe sugestões semelhantes  
- Based on Pokémon attributes such as HP, Attack, Defense, etc.

### ✅ Análise de Time / Team Analysis
- Insere até 6 Pokémon e vê um gráfico radar dos atributos médios  
- Insert up to 6 Pokémon and view a radar chart of average stats

---

## 🧠 Conceitos Didáticos Aplicados / Educational Concepts Applied

### 1. **APIs REST**
- Comunicação entre frontend e backend via HTTP  
- Communication between frontend and backend using HTTP

Endpoints:
- `POST /recommend/` – recomenda Pokémon / recommend Pokémon
- `POST /team_analysis/` – analisa o time / team stat analysis

### 2. **Requisições HTTP com `fetch()` / HTTP Requests using `fetch()`**
```js
fetch('/recommend/', {
  method: 'POST',
  body: JSON.stringify({ name: ["pikachu"], top_n: 5 }),
  headers: { 'Content-Type': 'application/json' }
})

3. Validação com Pydantic / Validation with Pydantic
python
Copiar
Editar
class PokemonRequest(BaseModel):
    name: List[str]
    top_n: int
4. Machine Learning com NearestNeighbors
Algoritmo de aprendizado não supervisionado para recomendação

Unsupervised learning algorithm used for recommendation

python
Copiar
Editar
from sklearn.neighbors import NearestNeighbors
model = NearestNeighbors(n_neighbors=top_n + 1)
model.fit(X)  # X = atributos normalizados / normalized stats
5. Manipulação de Dados com pandas / Data Handling with pandas
python
Copiar
Editar
filtered = df[df['name'].isin(team)]
mean_stats = filtered[stats].mean().tolist()
6. Frontend dinâmico com JS + Chart.js / Dynamic Frontend with JS + Chart.js
Gera gráficos interativos com base nos dados da API

Interactive charts generated with data from the API

7. Execução local com Uvicorn / Local Run with Uvicorn
bash
Copiar
Editar
uvicorn main:app --reload
📊 Exemplo de Uso / Usage Example
Digite o nome de um Pokémon e clique em "Recomendar"
Type a Pokémon name and click "Recommend"

Monte um time de até 6 Pokémon e clique em "Analisar Time"
Build a team of up to 6 Pokémon and click "Analyze Team"

Veja as recomendações ou o gráfico com os atributos médios
See recommendations or the radar chart of average stats

📁 Estrutura do Projeto / Project Structure
csharp
Copiar
Editar
├── main.py                 # API FastAPI
├── recommender.py         # Lógica de recomendação / Recommendation logic
├── pokedex_dataset.py     # Leitura do CSV / CSV Loader
├── pokemon.csv            # Base de dados / Dataset
├── templates/
│   └── index.html         # Interface Web / Web Interface
├── static/
│   └── style.css          # Estilo e JS / Styling and JS
🚀 Próximos Passos / Next Steps (Suggestions)
Adicionar imagens dos Pokémon no frontend
Add Pokémon images on frontend

Incluir tipos e fraquezas nas recomendações
Include types and weaknesses in recommendation

Publicar na nuvem (Render, Vercel, etc.)
Deploy to the cloud (Render, Vercel, etc.)