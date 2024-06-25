import os
import json as json


def listGen(input):
    dict = {}
    list = []
    str = input.strip(' ').split(' ')

    for index, item in enumerate(str):
        if (index % 2) == 0:
            dict["id"] = int(item)
        else:
            dict["chance"] = float(item)
            list.append(dict.copy())
    return list


"""
  
  Generate locationData.json from Locations.json

"""


def locations():
    with open('script_input/Locations.json', 'r') as file:
        my_list = []
        for line in file.readlines():
            # remove unnecessary characters
            rawList = line.replace('"', '').replace(
                ',', '').replace('\n', '').split('/')

            if line.__contains__(":"):
                # remove : seperator
                first = rawList[0].split(":")

                my_dict = {}

                my_dict["name"] = first[0].strip(' ')
                my_dict["spring_forage"] = listGen(first[1])
                my_dict["summer_forage"] = listGen(rawList[1])
                my_dict["fall_forage"] = listGen(rawList[2])
                my_dict["winter_forage"] = listGen(rawList[3])
                my_dict["spring_fish"] = listGen(rawList[4])
                my_dict["summer_fish"] = listGen(rawList[5])
                my_dict["fall_fish"] = listGen(rawList[6])
                my_dict["winter_fish"] = listGen(rawList[7])
                my_dict["artifacts"] = listGen(rawList[8])

                my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/locationData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
