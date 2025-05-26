import pandas as pd

# Load datasets
pokemon_df = pd.read_csv("final_pokemon.csv")
pokemon_df.info()
combats_df = pd.read_csv("final_combats.csv")
combats_df.info()

train_df = combats_df.merge(pokemon_df, left_on="First_pokemon", right_on="#")
train_df = train_df.merge(
    pokemon_df, left_on="Second_pokemon", right_on="#", suffixes=("_first", "_second")
)

train_df.drop(
    columns=["#_first", "#_second", "sprites_first", "sprites_second"], inplace=True
)

train_df.rename(
    columns={
        "First_pokemon": "First_pokemon_id",
        "Second_pokemon": "Second_pokemon_id",
    },
    inplace=True,
)

train_df.info()

train_df.to_csv('train.csv', index=False)
