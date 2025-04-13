from procyclingstats import Stage
from procyclingstats import Rider, Race, RiderResults, Team, RiderResults
import json
import csv
import pandas as pd

def get_ranking(player,race_name,year):
    # rider_results = RiderResults(f'rider/{player}/results')
    # print(json.dumps(rider_results.parse(),indent=4))
    # did_participate = False
    # for result in rider_results.parse()["results"]:
    #     if f'race/{race_name}/{year}/gc' == result["stage_url"]:
    #         return result["rank"]
    #     if f'race/{race_name}/{year}' in result["stage_url"]:
    #         did_participate = True
    # if did_participate:
    #     return "Did not finish"
    # return None

    stage = Stage(f'race/{race_name}/{year}/gc').results()
    for result in stage:
        if result["rider_url"]== f'rider/{player}':
            return result["rank"]
    # stage = Stage(f'race/{race_name}/{year}/stage-1').results()
    # for result in stage:
    #     print(result)
    #     if result["rider_url"]== f'rider/{player}':
    #         return result["status"]
    return None
        

def final_csv():
    WRITE_CSV = "final.csv"
    players = []
    with open("rider.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        players = [row for row in reader]

    
    with open("riddle.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        players += [row for row in reader]



if __name__ == "__main__":
    # stage = Stage("race/tour-de-france/2024/gc")
    # print(json.dumps(stage.results(),indent=4))
    print(get_ranking("primož-roglič","tour-de-france",2024))
    