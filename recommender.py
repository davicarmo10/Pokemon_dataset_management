import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import NearestNeighbors

#part of preparation of data using euclidean distance

def prepare_data(df):
    features = ['type1', 'type2', 'hp', 'attack', 'defense', 'sp.atk', 'sp.def', 'speed']
    
    df_features = df[features]

    categorical = ['type1', 'type2']
    numerical = ['hp', 'attack', 'defense', 'sp.atk', 'sp.def', 'speed']

    preprocessor = ColumnTransformer(transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical),
        ('num', StandardScaler(), numerical)
    ])

    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor)
    ])

    X = pipeline.fit_transform(df_features)

    model = NearestNeighbors(n_neighbors=6, algorithm='auto')
    model.fit(X)

    return X, df['name'].values, model, pipeline


def recommend_pokemon(name, top_n, df_pokedex, X, pokemon_names, model):
    index = df_pokedex[df_pokedex["name"] == name].index[0]
    distances, indices = model.kneighbors(X[index].reshape(1, -1), n_neighbors=top_n + 1)

    recommendations = []
    for i in indices[0][1:]:
        recommendations.append(pokemon_names[i])

    return recommendations

