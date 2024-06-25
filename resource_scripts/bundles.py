import os
import json as json


def bundleObjectGen(input):
    dict = {}
    list = []
    str = input.strip(' ').split(' ')

    for index, item in enumerate(str):
        if (index % 3) == 0:
            dict["id"] = item
        if (index % 3) == 1:
            dict["num_needed"] = int(item)
        elif (index % 3) == 2:
            dict["min_quality"] = int(item)
            list.append(dict.copy())
    return list


"""
  
  Generate bundleData.json from Bundles.json

"""


def bundles():
    with open('script_input/Bundles.json', 'r') as file:
        my_list = []
        for line in file.readlines():
            # remove unnecessary characters
            rawList = line.replace('"', '').replace(
                ',', '').replace('\n', '').split('/')

            if line.__contains__(":"):
                # remove : seperator
                first = rawList[1].split(":")

                my_dict = {}

                # formatting for reward returned
                reward_dict = {}
                reward = rawList[2].split(' ')
                if rawList[2] != '':
                    reward_dict["reward_type"] = reward[0]
                    reward_dict["reward_id"] = reward[1]
                    reward_dict["reward_count"] = int(reward[2])

                my_dict["room_name"] = rawList[0].strip(' ')
                my_dict["bundle_name"] = first[1].strip(' ')
                my_dict["reward"] = reward_dict
                my_dict["objects_needed"] = bundleObjectGen(rawList[3])
                if len(rawList) == 6:
                    my_dict["required_number"] = int(rawList[5])
                # my_dict["7"] = rawList[7] # not necessary at the moment

                my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/BundleData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
