import os
import json as json


def giftListGen(input):
    dict = {}
    list = []
    items = []
    if input == '':
        return []
    str = input.strip(' ').split(' ')
    for item in str:
        # dict["id"] = item
        list.append(item)
    return list


"""

  Generate giftData.json from NPCGiftTastes.json

"""


def giftData():
    with open('script_input/NPCGiftTastes.json', 'r') as file:
        my_list = []
        for line in file.readlines():

            # remove unnecessary characters
            rawList = line.replace('"', '').replace(
                ',', '').replace('\n', '').split('/')

            if line.__contains__(":"):
                # remove : seperator

                my_dict = {}

                first = rawList[0].split(":")
                if(first[0].__contains__('Universal')):
                    my_dict["name"] = first[0].strip(' ').replace('_', ' ')
                    my_dict["items"] = giftListGen(first[1])
                else:
                    my_dict["name"] = first[0].strip(' ')
                    my_dict["love"] = giftListGen(rawList[1])
                    my_dict["like"] = giftListGen(rawList[3])
                    my_dict["dislike"] = giftListGen(rawList[5])
                    my_dict["hate"] = giftListGen(rawList[7])
                    my_dict["neutral"] = giftListGen(rawList[9])

                my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/Gifts.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
