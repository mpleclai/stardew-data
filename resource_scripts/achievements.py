import os
import json as json

"""

    Generate achievementData.json from Achievements.json

"""


def achievements():
    with open('script_input/Achievements.json', 'r') as file:
        my_list = []
        for line in file.readlines():
            # remove unnecessary characters
            rawList = line.replace('"', '').replace(
                ',', '').replace('\n', '').split('^')

            if line.__contains__(":"):
                # remove : seperator
                first = rawList[0].split(":")
                my_dict = {}
                my_dict["id"] = int(first[0].strip(' '))
                my_dict["name"] = first[1].strip(' ')
                my_dict["description"] = rawList[1]
                my_dict["prereq"] = int(rawList[3])
                my_dict["hat_earned"] = int(rawList[4])

                my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/achievementData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
