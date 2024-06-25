import os
import json as json

"""

    Generate hatsData.json from Hats.json

"""


def hats():
    with open('script_input/Hats.json', 'r') as file:
        my_list = []
        for line in file.readlines():
            # remove unnecessary characters
            rawList = line.replace('"', '').replace(
                ',', '').replace('\n', '').split('/')

            if line.__contains__(":"):
                # remove : seperator
                first = rawList[0].split(":")
                my_dict = {}

                # format type and category
                tc_split = rawList[3].split(" ")
                category = 0
                if len(tc_split) > 1:
                    category = int(tc_split[1])

                my_dict["id"] = int(first[0].strip(' '))
                my_dict["name"] = first[1].strip(' ')
                my_dict["description"] = rawList[1]

                my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/hatsData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
