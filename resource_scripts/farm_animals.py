import os
import json as json

"""

  Generate farmAnimalData.json from FarmAnimals.json

"""


def farmAnimals():
    with open('script_input/FarmAnimals.json', 'r') as file:
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
                    my_dict["days_to_produce"] = int(first[1].strip(' '))
                    my_dict["days_til_mature"] = int(rawList[1])
                    my_dict["default_produce_id"] = int(rawList[2])
                    my_dict["deluxe_produce_id"] = int(rawList[3])
                    my_dict["harvest_type"] = int(rawList[13])
                    my_dict["building_type"] = rawList[15]
                    my_dict["fullness_drain"] = int(rawList[20])
                    my_dict["happiness_drain"] = int(rawList[21])
                    my_dict["harvest_tool"] = rawList[22]
                    my_dict["sell_price"] = int(rawList[24])

                    my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/farmAnimalData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
