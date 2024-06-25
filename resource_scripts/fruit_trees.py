import os
import json as json

"""

    Generate fruitTreeData.json from fruitTrees.json

"""


def fruitTrees():
    with open('script_input/fruitTrees.json', 'r') as file:
        my_list = []
        for line in file.readlines():
            # remove unnecessary characters
            rawList = line.replace('"', '').replace(
                ',', '').replace('\n', '').split('/')

            if line.__contains__(":"):
                # remove : seperator
                first = rawList[0].split(":")
                my_dict = {}
                my_dict["seed_id"] = int(first[0].strip(' '))
                my_dict["tree_index"] = int(first[1].strip(' '))
                my_dict["growth_season"] = rawList[1]
                my_dict["harvest_id"] = int(rawList[2])

                my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/fruitTreeData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
