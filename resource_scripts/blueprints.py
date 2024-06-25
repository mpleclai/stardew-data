import os
import json as json
from scripts.crafting_recipes import recipeListGen


"""

  Generate blueprintData.json from Blueprints.json

"""


def blueprints():
    with open('script_input/Blueprints.json', 'r') as file:
        my_list = []
        for line in file.readlines():

            # remove unnecessary characters
            rawList = line.replace('"', '').replace(
                ',', '').replace('\n', '').split('/')

            if line.__contains__(":"):
                # remove : seperator

                first = rawList[0].split(":")
                if(first[1].strip(' ') == 'animal'):
                    exit
                else:
                    my_dict = {}
                    my_dict["name"] = first[0].strip(' ')
                    if first[1].strip(' ') == '':
                        my_dict["items"] = []
                    else:
                        my_dict["items"] = recipeListGen(first[1].strip(' '))
                    my_dict["display_name"] = rawList[8]
                    my_dict["description"] = rawList[9]
                    my_dict["blueprint_type"] = rawList[10]
                    my_dict["upgrades_from"] = rawList[11]
                    my_dict["max_occupants"] = rawList[14]

                    if len(rawList) >= 18:
                        my_dict["price"] = int(rawList[17])
                        my_dict["instant_build"] = rawList[18]
                    else:
                        my_dict["price"] = []
                        my_dict["instant_build"] = []

                    my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/blueprintData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
