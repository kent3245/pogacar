import pandas as pd

# Read the CSV files
race_df = pd.read_csv('race_data_output.csv')
rider_df = pd.read_csv('rider.csv')
climb_df = pd.read_csv('climb_data_output.csv')

print(climb_df)
# Merge the race and climb data first on 'race_name'
race_climb_df = pd.merge(race_df, climb_df, on='race_name', how='left')

# Now merge rider data with the combined race/climb data.
# combined_df = pd.merge(rider_df, race_climb_df, on='race_name', how='inner')

df = pd.DataFrame(race_climb_df)

df.to_csv("combine.csv", index=False)
