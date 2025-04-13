from procyclingstats import RaceClimbs
import pandas as pd

# This list will store all the climb records from each race.
all_climb_data = []

# Open the CSV file with the correct encoding
with open("racename.csv", "r", encoding="utf-8") as file:
    # Iterate over each line in the file
    for line in file:
        race_name = line.strip()
        
        # Skip empty lines if any
        if not race_name:
            continue
        
        # Create an instance of RaceClimbs for the given race route
        try:
            # Adjust the URL as necessary for your API (here for 2024 route climbs)
            race_climb = RaceClimbs("race/" + race_name + "/2024/route/climbs")
        except Exception as e:
            print(f"Could not create RaceClimbs instance for {race_name}: {e}")
            continue
        
        try:
            climbs_table = race_climb.climbs("climb_name", "climb_url", "length", "steepness", "top", "km_before_finnish")
        except Exception as e:
            print(f"Failed to get climbs for {race_name}: {e}")
            climbs_table = []
        
        for climb in climbs_table:
            # Expect each climb record to be a dictionary. Add the race name.
            climb["race_name"] = race_name
            all_climb_data.append(climb)

df = pd.DataFrame(all_climb_data)

df.to_csv("climb_data_output.csv", index=False)
