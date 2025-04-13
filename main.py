from procyclingstats import Rider, Race
import json

# Open the CSV file with the correct encoding
with open("rider.csv", "r", encoding="utf-8") as file:
    # Iterate over each line in the file
    for line in file:
        # Clean up whitespace/newline characters
        rider_name = line.strip()
        
        # Skip empty lines if any
        if not rider_name:
            continue
        
        # Create an instance of Rider. Assuming the structure "rider/<rider_name>"
        rider = Rider("rider/" + rider_name)
        
        # Debug: print the type to confirm the instance creation
        print("Rider instance type for {}: {}".format(rider_name, type(rider)))

        print("Points per Season:", rider.points_per_season_history())
        print("Points per Speciality:", rider.points_per_speciality())



def add_col(lists,):
    """adds column by columnm"""
