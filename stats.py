from procyclingstats import Stage
from procyclingstats import Rider, Race, RiderResults, Team, RiderResults
import json
import csv
import pandas as pd
# from main import get_ranking
import unicodedata

def remove_accents(input_str):
    # Normalize the string to decompose accents
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    # Filter out combining characters (accents)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])


def get_ranking(player,race_name,year):
    # try:
    #     stage = Stage(f'race/{race_name}/{year}/gc').results()
    #     # print(json.dumps(stage,indent=4))
    #     for result in stage:
    #         if remove_accents(result["rider_url"])== remove_accents(f'rider/{player}'):
    #             return result["rank"]
    # except Exception as e:
    #     stage = Stage(f'race/{race_name}/{year}/result').results()
    #     # print(json.dumps(stage,indent=4))
    #     for result in stage:
    #         # print(remove_accents(result["rider_url"]))
    #         # print(remove_accents(f'rider/{player}'))
    #         if remove_accents(result["rider_url"]) == remove_accents(f'rider/{player}'):
    #             return result["rank"]
    # return None
    print(player,race_name,year)
    stage = Stage(f'race/{race_name}/{year}/gc').results()
    for result in stage:
        print(result["rider_url"])
        print(result["rider_name"])
        if result["rider_url"] == "rider/remco-evenepoel":
            print(result)
            break
        

def final_csv():
    WRITE_CSV = "final.csv"
    players = []
    players_header = ["name", "team", "age", "height", "weight", "birthdate", "years pro"]
    with open("rider.csv", "r", encoding="utf-8") as csv_file:  # Specify UTF-8 encoding
        reader = csv.reader(csv_file)
        header = next(reader)  # Skip the header line
        players = [row for row in reader]

    combine_header = ["race_name", "category", "climb_name", "climb_url", "length", "steepness", "top", "km_before_finnish"]
    combine = []
    with open("combine.csv", "r", encoding="utf-8") as csv_file:  # Specify UTF-8 encoding
        reader = csv.reader(csv_file)
        header = next(reader)
        combine = [row for row in reader]
    print(players)
    print("com",combine)
    with open("final.csv", "w", newline="", encoding="utf-8") as csv_file:  # Specify UTF-8 encoding
        writer = csv.writer(csv_file)
        # Write the header
        writer.writerow(players_header + combine_header + ["rank"])
        # Write the data
        for player in players:
            for race in combine:
                print('------------------')
                print(player[0],race[0])
                ranking = get_ranking(player[0], race[0], 2024)
                print(ranking)
                writer.writerow(player + race + [ranking])
                print('------------------')
    



if __name__ == "__main__":
    # stage = Stage("race/tour-de-france/2024/gc")
    # print(json.dumps(stage.results(),indent=4))
    # print(ge    print(get_ranking("remco-evenepoel","paris-nice",2024))
    print(get_ranking("remco-evenepoel","paris-nice",2024))

    # final_csv()

