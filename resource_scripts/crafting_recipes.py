import os
import json as json


def recipeListGen(input):
    dict = {}
    list = []
    str = input.strip(' ').split(' ')
    if input.__contains__(' '):
        for index, item in enumerate(str):
            if (index % 2) == 0:
                dict["id"] = int(item)
            else:
                dict["quantity"] = int(item)
                list.append(dict.copy())
    else:
        dict["id"] = int(input)
        dict["quantity"] = 1
        list.append(dict.copy())
    return list


"""
  
  Generate craftingRecipeData.json from CraftingRecipes.json

"""


def craftingRecipes():
    with open('script_input/CraftingRecipes.json', 'r') as file:
        my_list = []
        for line in file.readlines():

            # remove unnecessary characters
            rawList = line.replace('"', '').replace(
                ',', '').replace('\n', '').split('/')
            if rawList[0].__contains__('Warp Totem:'):
                rawList[0] = rawList[0].replace('Warp Totem:', 'Warp Totem')

            if line.__contains__(":"):
                # remove : seperator

                first = rawList[0].split(":")

                my_dict = {}

                my_dict["name"] = first[0].strip(' ')
                my_dict["ingredients"] = recipeListGen(first[1])
                my_dict["yield"] = recipeListGen(rawList[2])
                my_dict["is_big_craft"] = rawList[3]
                # my_dict["unlock_conditions"] = rawList[4]
                my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/craftingRecipesData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
