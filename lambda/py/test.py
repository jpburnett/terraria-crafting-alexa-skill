#--------------------------------------------------------------------------
# Resource Libraries
#--------------------------------------------------------------------------
from resources import data, util

my_recipes = data.ITEMS

#Get the random item
item_name = util.get_random_item()

recipe = my_recipes[item_name]

print(item_name)
print(recipe)