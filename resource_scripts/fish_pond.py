import os


def fishPond():
    directory = "script_output/fishPondData.json"
    os.makedirs(os.path.dirname(directory), exist_ok=True)

    with open('script_input/FishPondData.json', 'r') as file, open(directory, 'w') as output:
        for line in file:
            if line.__contains__('item_'):
                line = line.replace('item_', '').replace('_', ' ')
            output.write(line)
