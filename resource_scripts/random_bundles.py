import os


def randomBundles():
    directory = "script_output/randomBundleData.json"
    os.makedirs(os.path.dirname(directory), exist_ok=True)

    with open('script_input/RandomBundles.json', 'r') as file, open(directory, 'w') as output:
        for line in file:
            output.write(line)
