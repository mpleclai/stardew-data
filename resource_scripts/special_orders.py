import os


def specialOrders():
    directory = "script_output/specialOrdersData.json"
    os.makedirs(os.path.dirname(directory), exist_ok=True)

    with open('script_input/SpecialOrders.json', 'r') as file, open(directory, 'w') as output:
        for line in file:
            output.write(line)
