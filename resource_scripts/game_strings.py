import os
import json as json

"""
  
  Generate GameStrings.strings from game string files

"""
# 'script_input/ObjectStrings.json'
# "script_output/ObjectStrings.strings"


def gameStrings(inputPath, outputPath):
    with open(inputPath, 'r') as file:
        data = file.read()
        data = data.replace(",", ";").replace(':', '=')
        data = data.strip('{')

        # make script_output directory data file
        os.makedirs(os.path.dirname(outputPath), exist_ok=True)

        # write JSON file from generated list to the new output folder
        with open(outputPath, 'w') as output:
            output.write(data)
