import pandas as pd

# Load datasets
pokemon_df = pd.read_csv("train2.csv")
pokemon_df.info()

# Combining the stats of both Pokémon into a single DataFrame
pokemon_df['Total_stats_first'] = (
    pokemon_df['HP_first'] +
    pokemon_df['Attack_first'] +
    pokemon_df['Defense_first'] +
    pokemon_df['Sp. Atk_first'] +
    pokemon_df['Sp. Def_first'] +
    pokemon_df['Speed_first']
)

pokemon_df['Total_stats_second'] = (
    pokemon_df['HP_second'] +
    pokemon_df['Attack_second'] +
    pokemon_df['Defense_second'] +
    pokemon_df['Sp. Atk_second'] +
    pokemon_df['Sp. Def_second'] +
    pokemon_df['Speed_second']
)

pokemon_df.drop(columns=['HP_first','Attack_first','Defense_first','Sp. Atk_first','Sp. Def_first','Speed_first','HP_second','Attack_second','Defense_second','Sp. Atk_second','Sp. Def_second','Speed_second'], inplace=True)


# Reducing features
# Assign using loc
pokemon_df.loc[:, 'Experience_diff'] = pokemon_df['base_experience_first'] - pokemon_df['base_experience_second']

pokemon_df.loc[:, 'Height_diff'] = pokemon_df['height_first'] - pokemon_df['height_second']

pokemon_df.loc[:, 'Weight_diff'] = pokemon_df['weight_first'] - pokemon_df['weight_second']

pokemon_df.loc[:, 'Generation_diff'] = pokemon_df['Generation_first'] - pokemon_df['Generation_second']

pokemon_df.loc[:, 'Legendary_diff'] = pokemon_df['Legendary_first'] - pokemon_df['Legendary_second']

pokemon_df.loc[:, 'Total_stats_diff'] = pokemon_df['Total_stats_first'] - pokemon_df['Total_stats_second']

# Drop the original columns
# Then drop only columns that exist
cols_to_drop = ['base_experience_first', 'height_first', 'weight_first', 
               'Generation_first', 'Legendary_first', 'Total_stats_first',
               'base_experience_second', 'height_second', 'weight_second',
               'Generation_second', 'Legendary_second', 'Total_stats_second']

pokemon_df.drop(columns=[col for col in cols_to_drop if col in pokemon_df.columns], 
               inplace=True)

# Rearranging columns: 
pokemon_df = pokemon_df[['First_pokemon_id', 'Type 1_first', 'Type 2_first','Second_pokemon_id','Type 1_second','Type 2_second','Height_diff','Weight_diff','Experience_diff','Total_stats_diff','Generation_diff','Legendary_diff', 'Winner']]

pokemon_df.to_csv('train3.csv', index=False)