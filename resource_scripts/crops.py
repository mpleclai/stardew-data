import os
import json as json
"""
  
  Generate cropData.json from Crops.json

"""


def crops():
    with open('script_input/Crops.json', 'r') as file:
        my_list = []
        for line in file.readlines():
            # remove unnecessary characters
            rawList = line.replace('"', '').replace(
                ',', '').replace('\n', '').split('/')

            if line.__contains__(":"):
                # remove : seperator
                first = rawList[0].split(":")

                # format growth stage days
                stage_dict = {}
                stage_days = first[1].strip(' ').split(' ')
                i = 0
                for stage in stage_days:
                    stage_dict["stage" + str(i)] = int(stage)
                    i = i+1

                # format extra harvest chance
                harvest_dict = {}
                chance = rawList[6].split(" ")
                chanceTrue = rawList[6].__contains__("true")

                if chanceTrue:
                    harvest_dict["min_harvest"] = int(chance[1])
                    harvest_dict["max_harvest"] = int(chance[2])
                    harvest_dict["max_harvest_increase"] = int(chance[3])
                    harvest_dict["extra_crop_chance"] = float(chance[4])

                if chanceTrue:
                    harvest_chance = chance[0]
                else:
                    harvest_chance = rawList[6]

                my_dict = {}

                my_dict["seed_id"] = int(first[0].strip(' '))
                my_dict["growth_stage"] = stage_dict
                my_dict["season"] = rawList[1]
                my_dict["harvest_id"] = int(rawList[3])
                my_dict["regrows"] = int(rawList[4])
                my_dict["harvest_method"] = int(rawList[5])
                my_dict["raised_seeds"] = rawList[7]
                my_dict["extra_harvest_chance"] = harvest_chance
                my_dict["chance_data"] = harvest_dict

                # my_dict["tint_color"] = rawList[8]

                my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/cropData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
