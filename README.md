////  IN PROGRESS -- NOT FUNCTIONAL ////

<!-- To run 

 pip3 install requests 

You will have to modify the default game path variable to wherever you have it stored on your computer -->

Python script to generate re-formatted data from the game files for easier consumption.

Detailed information on the input JSON structure is found here: [https://stardewvalleywiki.com/Modding:Index](https://stardewvalleywiki.com/Modding:Index])

To get input files follow the steps here to unpack the games XNB files: https://stardewvalleywiki.com/Modding:Editing_XNB_files#StardewXnbHack 

To run:
1. Ensure all necessary input files are in script_input
2. Run `python3 parse.py`
3. The output files will appear in script_output

Note: Existing parsing for input files needs to be updated to reflect 1.6 changes.
