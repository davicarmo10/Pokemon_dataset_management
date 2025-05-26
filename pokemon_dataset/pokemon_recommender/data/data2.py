import pandas as pd

# Load datasets
pokemon_df = pd.read_csv("train.csv")
pokemon_df.info()

#converting legendary bool columns to int
pokemon_df['Legendary_first'] = pokemon_df['Legendary_first'].astype(int)
pokemon_df['Legendary_second'] = pokemon_df['Legendary_second'].astype(int)

# Drop unnecessary columns for the model
pokemon_df.drop(['Name_first', 'Name_second'], axis=1, inplace=True)

#Label encoding categorical columns
pokemon_df['Type 1_first'].unique()
#pokemon_df['Type 1_first'].nunique()
#pokemon_df['Type 1_first'].value_counts()

pokemon_df['Type 2_first'].unique()
#pokemon_df['Type 2_first'].nunique()
#pokemon_df['Type 2_first'].value_counts()

pokemon_df['Type 1_second'].unique()
#pokemon_df['Type 1_second'].nunique()
#pokemon_df['Type 1_second'].value_counts()

pokemon_df['Type 2_second'].unique()
#pokemon_df['Type 2_second'].nunique()
#pokemon_df['Type 2_second'].value_counts()

sorted(pokemon_df['Type 1_first'].unique().tolist())

# Manual mapping: Pokémon types to integers (in sorted order)
type_mapping = {
    'Bug': 0,
    'Dark': 1,
    'Dragon': 2,
    'Electric': 3,
    'Fairy': 4,
    'Fighting': 5,
    'Fire': 6,
    'Flying': 7,
    'Ghost': 8,
    'Grass': 9,
    'Ground': 10,
    'Ice': 11,
    'Normal': 12,
    'Poison': 13,
    'Psychic': 14,
    'Rock': 15,
    'Steel': 16,
    'Water': 17
}

# Apply manual mapping to the types columns
pokemon_df['Type 1_first'] = pokemon_df['Type 1_first'].map(type_mapping)
pokemon_df['Type 2_first'] = pokemon_df['Type 2_first'].map(type_mapping)
pokemon_df['Type 1_second'] = pokemon_df['Type 1_second'].map(type_mapping)
pokemon_df['Type 2_second'] = pokemon_df['Type 2_second'].map(type_mapping)

# View the updated DataFrame
print(pokemon_df)

pokemon_df.to_csv('train2.csv', index=False)