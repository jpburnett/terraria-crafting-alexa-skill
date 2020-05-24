#--------------------------------------------------------------------------
# Resource Libraries
#--------------------------------------------------------------------------
from resources import data, util

list_of_items = data.ITEMS

#Get the random item
item_name = "Torch"

item_name = item_name.lower()
print("The item I am looking for is", item_name)

list_of_items = {k.lower(): v for k, v in list_of_items.items()}

if item_name in list_of_items:
    recipe = list_of_items[item_name]
    print(recipe)