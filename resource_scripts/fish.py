import os
import json as json
"""
  
  Generate fishData.json from Fish.json

"""


def fish():
    with open('script_input/Fish.json', 'r') as file:
        my_list = []
        for line in file.readlines():
            # remove unnecessary characters
            rawList = line.replace('"', '').replace(
                ',', '').replace('\n', '').split('/')

            # remove : seperator
            if line.__contains__(":"):
                for item in rawList:
                    if(item != rawList[5]):
                        item.replace(' ', '')
                first = rawList[0].split(":")

                my_dict = {}
                time_dict = {}
                # Consider alternate format for trap vs normal fish
                if line.__contains__("trap"):  # is trap fish
                    my_dict["id"] = first[0].strip(' ')
                    my_dict["name"] = first[1].strip(' ')
                    my_dict["type"] = rawList[1]
                    my_dict["chance"] = float(rawList[2])
                    my_dict["location"] = rawList[4]
                else:  # is normal fish

                    # Seperate times into their own dictionary to be a sub-list
                    times = rawList[5].strip('"').split(" ")
                    time_dict["min_time"] = int(times[0])
                    time_dict["max_time"] = int(times[1])

                    my_dict["id"] = first[0].strip(' ')
                    my_dict["name"] = first[1].strip(' ')
                    my_dict["chance_to_dart"] = int(rawList[1])
                    my_dict["darting_randomness"] = rawList[2]
                    my_dict["time"] = time_dict
                    my_dict["weather"] = rawList[7]
                    my_dict["fishing_level"] = int(rawList[12])
                my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/Fish.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))

        # var location: String
        # var locationArea: String
        # var season: String
        # var isUnique: String -----?
