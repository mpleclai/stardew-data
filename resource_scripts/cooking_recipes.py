import os
import json as json
from scripts.crafting_recipes import recipeListGen

"""
  
  Generate cookingRecipeData.json from CookingRecipes.json

"""


def cookingRecipes():
    with open('script_input/CookingRecipes.json', 'r') as file:
        my_list = []
        for line in file.readlines():

            # remove unnecessary characters
            rawList = line.replace('"', '').replace(
                ',', '').replace('\n', '').split('/')

            if line.__contains__(":"):
                # remove : seperator

                first = rawList[0].split(":")

                my_dict = {}

                my_dict["name"] = first[0].strip(' ')
                my_dict["ingredients"] = recipeListGen(
                    first[1])
                my_dict["yield"] = recipeListGen(rawList[2])
                # my_dict["unlock_conditions"] = rawList[3]
                my_list.append(my_dict)

        # make script_output directory with JSON data file
        directory = "script_output/cookingRecipesData.json"
        os.makedirs(os.path.dirname(directory), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(directory, 'w') as output:
            output.write(json.dumps(my_list, indent=2))
