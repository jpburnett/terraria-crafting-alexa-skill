# -*- coding: utf-8 -*-

# Resolving gettext as _ for module loading.
from gettext import gettext as _

SKILL_NAME = _("Terraria Tool")
WELCOME_MESSAGE = _("Welcome to {}. You can ask me something like, what's the recipe for a {}? ... Now, what can I help you craft?")
WELCOME_REPROMPT = _("For instructions on what you can say, please say help.")
DISPLAY_CARD_TITLE = _("{}  - Recipe for {}.")
HELP_MESSAGE = _("You can ask, what's the recipe for a {}, or, you can say exit...So, what can I help you craft?")
HELP_REPROMPT = _("You can say things like, what's the recipe for a {}, or you can say exit...So, what can I help you craft?")
FALLBACK_MESSAGE = _("The {} skill can't help you with that.")
STOP_MESSAGE = _("Happy Crafting!")
RECIPE_REPEAT_MESSAGE = _("Try saying repeat.")
RECIPE_NOT_FOUND_MESSAGE = _("I'm sorry, I currently do not know ")
RECIPE_NOT_FOUND_WITH_ITEM_NAME = _("the recipe for {}. ")
RECIPE_NOT_FOUND_WITHOUT_ITEM_NAME = _("that recipe. ")
RECIPE_NOT_FOUND_REPROMPT = _("What else can I help with?")

RECIPE_EN_US = {
    # Furniture
    "wood door": "a wood door is made with 6 wood while standing by a crafting table",
    "wood chair": "a wood chair is made with 4 wood while standing by a crafting table",
    "wood table": "a wood table is made with 8 wood while standing by a crafting table",
    "sign": "a sign is crafted with with 6 wood while standing by a crafting table",
    "chest": "a chest is made with 8 wood and 2 iron bars while near a crafting table",
    "candle": "a candle is made with 1 gold bar and 1 torch",
    "furnace": "A furnace can be crafted by using twenty stone blocks, four wood, and three torches",
    "iron anvil": "An iron anvil requires five iron bars and you need to stand near a work bench.",
    "fish bowl": "a fish bowl is made with 2 goldfish and 1 bottled water",
    "sawmill": "a sawmill is crafted with 10 wood, 2 iron bars and 1 iron chain",
    "tiki torch": "a tiki torch is made with 3 wood and 1 torch",
    "statue": "a statue is made with 100 stone blocks",
    # Misc
    "slime": "slime can be obtained by killing slime enemies.",
    "stone": "Stone is fairly common and can be mined from the ground in several areas of the map.",
    "sand": "Sand can be found in the desert biome or at the beach on the far left or right of the map.",
    "clay": "clay is found most commonly at the surface and is a slightly darker color than dirt.",
    "copper": "copper ore can be found on the surface, in the cavern biome, or underground and can be mined with any pickaxe.",
    "tin": "tin ore can be found on or near the surface, in the cavern biome or underground and can be mined with any pickaxe.",
    "iron": "iron can be found underground or in the cavern biome and can be mined with any pickaxe.",
    "platinum": "platinum can be found underground",
    "demonite": "demonite ore can be found in the corruption areas and mined with a gold pickaxe or better. Defeating bosses also dropes the ore.",
    "meteorite": "meteorite ore can be found at a Meteorite crash site. A Meteorite crash site has a 50% chance of spawning the next midnight after a Shadow Orb or Crimson Heart is smashed.",
    "wood": "Wood can be obtained by chopping down a tree with an axe.",
    # Torches?...
    "torch": "A torch can be crafted with one gel and one wood",
    "cursed torch": "cursed torches are made with 33 torches and 1 cursed flame",
    "blue torch": "blue torches are made with 3 torches and 1 sapphire",
    "red torch": "red torches are made with 3 torches and 1 ruby",
    "green torch": "green torches are made with 3 torches and 1 emerald",
    "purple torch": "purple torches are made with 3 torches and 1 amethyst",
    "white torch": "white torches are made with 3 torches and 1 diamond",
    # Weapons and stuff
    "iron pickaxe": "An iron pickaxe can be crafted by using three wood and 12 iron bars at any anvil.",
    "iron broadsword": "An iron broadsword can be crafted by using 8 iron bars at any anvil.",
    "work bench": "A work bench can be made with ten wood",
    "cobalt bar": "a cobalt bar is made by smelting three cobalt ore at a furnace.",
    "iron bar": "An iron bar can be made using the furnace to smelt three iron ore.",
    "meteorite bar": "A meteorite bar can be made using the furnace to smelt three meteorite ore.",
    "platinum bar": "A platinum bar can be made using the furnace to smelt four platinum ore.",
    "demonite bar": "A demonite bar can be made using the furnace to smelt three demonite ore.",
    "gold bar": "A gold bar can be made using the furnace to smelt three gold ore",
    "copper bar": "A copper bar can be made using the furnace to smelt three copper ore",
    "tin bar": "A tin bar can be made using the furnace to smelt three tin ore",
    "grey brick": "grey brick can be made by using 2 stone at a furnace.",
    "red brick": "red brick can be made by using 2 clay at a furnace.",
    "shadow orb": "A Shadow Orb is a floating purple sphere, and can be found deep in The Corruption areas.",
    "bottle": "A bottle can be made by using 1 glass block at a furnace",
    "mana crystal": "a mana crystal is made using three fallen stars.",
    "fallen star": "fallen stars randomly fall from the sky at night.",
    "sticky glowstick": "sticky glowsticks are made with gel and a glowstick",
    "sticky bomb": "sticky bomb is made with a bomb and gel",
    "sticky grenade": "sticky grenade is made with a grenade and gel",
    "heart lantern": "a heart lantern is made with a life crystal and 4 chain",
    "life crystal": "a life crystal can be found in underground caverns",
    "rope coil": "rope coil is made with 10 rope",
    "soul of fright": "soul of fright is dropped by defeating skeletron prime",
    "holy water": "holy water requires 5 pixie dust, 1 bottled water and 1 hallowed seeds",
    "unholy water": "unholy water requires 1 bottled water, 1 corrupt seeds and 1 ebonsand block",
    "": ""
}
