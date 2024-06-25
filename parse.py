import json as json
from tokenize import Double
from resource_scripts.boots import boots
from resource_scripts.bundles import bundles
from resource_scripts.big_craftables import bigCraftables
from resource_scripts.object_information import objectInformation
from resource_scripts.crops import crops
from resource_scripts.fish import fish
from resource_scripts.locations import locations
from resource_scripts.hats import hats
from resource_scripts.weapons import weapons
from resource_scripts.clothing import clothing
from resource_scripts.furniture import furniture
from resource_scripts.crafting_recipes import craftingRecipes
from resource_scripts.cooking_recipes import cookingRecipes
from resource_scripts.tailoring_recipes import tailoringRecipes
from resource_scripts.blueprints import blueprints
from resource_scripts.random_bundles import randomBundles
from resource_scripts.fish_pond import fishPond
from resource_scripts.special_orders import specialOrders
from resource_scripts.fruit_trees import fruitTrees
from resource_scripts.farm_animals import farmAnimals
from resource_scripts.monsters import monsters
from resource_scripts.achievements import achievements
from resource_scripts.quests import quests
from resource_scripts.gift_tastes import giftData
from resource_scripts.game_strings import gameStrings

achievements()
quests()
giftData()
# craftingRecipes()
# cookingRecipes()
# tailoringRecipes()
# blueprints() -- renamed to buildings --consumable by default
# locations()
# crops() --consumable by default
# fruitTrees() -- consumable by default
fish()
fishPond()
# farmAnimals() -- consumable by default
# monsters()
# objectInformation() -- conusmable by default
# bigCraftables()
furniture()
# boots()
# hats()
# clothing()
# weapons()
bundles()
# randomBundles()
# specialOrders()


# Strings Example
# gameStrings('script_input/ObjectStrings.json', "script_output/ObjectStrings.strings")
