import os
import json as json

"""
  
  Generate bootsData.json from Boots.json

"""


def boots():
    with open('script_input/Boots.json', 'r') as file:
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
                my_dict["defense"] = int(rawList[3])
                my_dict["immunity"] = int(rawList[4])

                my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/bootsData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
