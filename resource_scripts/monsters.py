import os
import json as json
from scripts.locations import listGen


"""

  Generate monsterData.json from Monsters.json

"""


def monsters():
    with open('script_input/Monsters.json', 'r') as file:
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
                    my_dict["health"] = int(first[1].strip(' '))
                    my_dict["attack_damage"] = int(rawList[1])
                    my_dict["flying"] = rawList[4]
                    my_dict["drops"] = listGen(rawList[6])
                    my_dict["defense"] = int(rawList[7])
                    my_dict["speed"] = rawList[10]
                    my_dict["mine_monster"] = rawList[12]
                    my_dict["exp_gain"] = int(rawList[13])

                    my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/monsterData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
