
from procyclingstats import Rider, Race
import json
import csv
import pandas as pd

# Open the CSV file with the correct encoding
# with open("rider.csv", "r", encoding="utf-8") as file:
#     # Iterate over each line in the file
#     for line in file:
#         # Clean up whitespace/newline characters
#         rider_name = line.strip()
        
#         # Skip empty lines if any
#         if not rider_name:
#             continue
        
#         # Create an instance of Rider. Assuming the structure "rider/<rider_name>"
#         rider = Rider("rider/" + rider_name)
        
#         # Debug: print the type to confirm the instance creation
#         print("Rider instance type for {}: {}".format(rider_name, type(rider)))

#         print("Points per Season:", rider.points_per_season_history())
#         print("Points per Speciality:", rider.points_per_speciality())




def add_col(lists,path_name):
    """adds column by columnm"""
    with open(path_name, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = [row for row in reader]

    # Ensure the number of rows matches the length of the new column
    if len(rows) != len(lists):
        raise ValueError("The number of rows in the CSV file does not match the length of the new column.")

    # Add the new column to each row
    for i, row in enumerate(rows):
        row.append(lists[i])

    # Write the updated data back to the CSV file
    with open(path_name, 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def add_birth():
    with open("rider.csv", "r", encoding="utf-8") as file:
        # Iterate over each line in the file
        file.readline()  # Skip the header line
        lists = []
        for line in file:
            # Clean up whitespace/newline characters
            rider_name = line.split(",")[0].strip()
            
            # Skip empty lines if any
            if not rider_name:
                continue
            
            # Create an instance of Rider. Assuming the structure "rider/<rider_name>"
            print("rider/" + rider_name)
            rider = Rider("rider/" + rider_name)
            try:
                rider_data = rider.parse()
                lists.append(min(2025,max(year["season"] for year in rider_data["teams_history"] if year["season"]))-min(year["season"] for year in rider_data["teams_history"] if year["season"]))
            except Exception as e:
                lists.append(None)
    return lists

def get_shit():
    rider = Rider("rider/matteo-trentin")
    # Get and print the rider's birthdate
    print(rider)
    # Alternatively, you can parse all available data
    print(rider.teams_history())
    # rider_data = rider.parse()
    # print(json.dumps(rider_data, indent=4))


    # print(min(year["season"] for year in rider_data["teams_history"] if year["season"]))


def get_metric():
    rider = Rider("rider/tadej-pogacar")
    rider_dict = rider.points_per_speciality()
    print(rider_dict)
    path_name = "rider.csv"
    # for key,value in rider_dict.items():    
    lists = add_birth()
    lists.insert(0,"years pro")
    print(lists)
    add_col(lists, path_name)


if __name__ == "__main__":
    # Example usage of the add_col function

    # print("Columns added successfully.")
    get_metric()

#     df = pd.read_csv('rider.csv')

# # Drop the column named 'column_to_erase'
#     df = df.drop(columns=['years pro'])
#     df.to_csv('rider.csv', index=False)

    # # Get and print the rider's birthdate
    # print("Rider Birthdate:", rider.birthdate())

    # # Alternatively, you can parse all available data
    # rider_data = rider.parse()
    # print(json.dumps(rider_data, indent=4))
