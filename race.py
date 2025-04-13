from procyclingstats import Race
import pandas as pd

# Initialize an empty list to store race info
race_data = []

# Open the CSV file with the correct encoding
with open("racename.csv", "r", encoding="utf-8") as file:
    # Iterate over each line in the file
    for line in file:
        # Clean up whitespace/newline characters
        race_name = line.strip()
        
        # Skip empty lines if any
        if not race_name:
            continue
        
        # Create an instance of Race using fallback URLs
        try:
            race = Race("race/" + race_name + "/2024/gc")
        except Exception:
            try:
                race = Race("race/" + race_name + "/2024/result")
            except Exception:
                race = Race("race/" + race_name + "/2024")
        
        # Get the traits from the Race object
        one_day = race.is_one_day_race()
        race_category = race.category()
        
        # Append the data as a dictionary
        race_data.append({
            "race_name": race_name,
            "category": race_category,
        })

# Create a pandas DataFrame from the collected data
df = pd.DataFrame(race_data)

# Optionally, if you want to check or export the DataFrame, you can print it or save to CSV
df.to_csv("race_data_output.csv", index=False)
