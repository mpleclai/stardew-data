import os
import json as json

"""
  
  Generate objectInformationData.json from ObjectInformation.json

"""


def objectInformation():
    with open('script_input/ObjectInformation.json', 'r') as file:
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
                my_dict["price"] = int(rawList[1])
                my_dict["edibility"] = int(rawList[2])
                my_dict["type"] = tc_split[0]
                my_dict["category"] = category
                my_dict["display_name"] = rawList[4]
                my_dict["description"] = rawList[5]

                # rawList[6] and rawList[7] and rawList[8] don't seem to be pertinent at the moment

                # if len(rawList) == 7:
                #     if()
                #     my_dict["misc1"] = rawList[6]

                # if len(rawList) == 8:
                #     my_dict["misc1"] = rawList[6]
                # my_dict["misc2"] = rawList[7]

                # if len(rawList) == 9:
                #     # my_dict["misc1"] = rawList[6]
                #     # my_dict["misc2"] = rawList[7]
                #     my_dict["buff_duration"] = int(rawList[8])

                my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/objectInformationData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
