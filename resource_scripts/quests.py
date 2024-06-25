import os
import json as json

"""

    Generate questData.json from Quests.json

"""


def quests():
    with open('script_input/Quests.json', 'r') as file:
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
                my_dict["type"] = first[1].strip(' ')
                my_dict["title"] = rawList[1]
                my_dict["details"] = rawList[2]
                my_dict["condition"] = rawList[3]
                my_dict["trigger"] = rawList[4]
                my_dict["next_quest"] = rawList[5]
                my_dict["gold"] = int(rawList[6])

                my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/questData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
