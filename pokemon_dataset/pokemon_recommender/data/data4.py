import pandas as pd

# Load datasets
pokemon_df = pd.read_csv("train3.csv")
pokemon_df.info()

# Target: 1 if first Pokémon wins, 0 if second wins
pokemon_df['Winner'] = (pokemon_df['Winner'] == pokemon_df['First_pokemon_id']).astype(int)

# Drop them from training
pokemon_df = pokemon_df.drop(['First_pokemon_id', 'Second_pokemon_id'], axis=1)

pokemon_df.to_csv('train4.csv', index=False)