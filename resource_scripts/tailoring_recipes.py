import os


def tailoringRecipes():
    directory = "script_output/tailoringRecipeData.json"
    os.makedirs(os.path.dirname(directory), exist_ok=True)

    with open('script_input/TailoringRecipes.json', 'r') as file, open(directory, 'w') as output:
        for line in file:
            output.write(line)
