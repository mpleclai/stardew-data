import os
import json as json

"""
  
  Generate clothingData.json from ClothingInformation.json

"""


def clothing():
    with open('script_input/ClothingInformation.json', 'r') as file:
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
                my_dict["description"] = rawList[2]
                my_dict["price"] = int(rawList[5])
                my_dict["dyeable"] = rawList[7]
                my_dict["type"] = rawList[8]

                my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/clothingData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
