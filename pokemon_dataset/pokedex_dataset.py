import pandas as pd

def load_data_pokedex(caminho_csv: str):
    df = pd.read_csv(caminho_csv)
    print(df.head())
    print("\nColunas disponíveis:")
    print(df.columns)
    return df
