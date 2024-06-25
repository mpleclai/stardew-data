import os
import json as json

"""
  
  Generate weaponsData.json from Weapons.json

"""


def weapons():
    with open('script_input/weapons.json', 'r') as file:
        my_list = []
        for line in file.readlines():
            # remove unnecessary characters
            rawList = line.replace('"', '').replace(
                ',', '').replace('\n', '').split('/')

            if line.__contains__(":"):
                # remove : seperator
                first = rawList[0].split(":")
                my_dict = {}

                my_dict["id"] = int(first[0].strip(' '))
                my_dict["name"] = first[1].strip(' ')
                my_dict["description"] = rawList[1]
                my_dict["min_damage"] = int(rawList[2])
                my_dict["max_damage"] = int(rawList[3])
                my_dict["knockback"] = float(rawList[4])
                my_dict["speed"] = int(rawList[5])
                my_dict["precision"] = int(rawList[6])
                my_dict["defence"] = int(rawList[7])
                my_dict["type"] = int(rawList[8])
                my_dict["base_mine_lvl"] = int(rawList[9])
                my_dict["min_mine_lvl"] = int(rawList[10])
                my_dict["aoe"] = int(rawList[11])
                my_dict["critical_chance"] = float(rawList[12])
                my_dict["critical_damage"] = float(rawList[13])

                my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/weaponsData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
