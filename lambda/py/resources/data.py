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
    "torch": "A torch can be crafted with one gel and one wood",
    "furnace": "A furnace can be crafted by using twenty stone blocks, four wood, and three torches",
    "iron anvil": "An iron anvil requires five iron bars and you need to stand near a work bench.",
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
    "fallen star": "fallen stars randomly fall from the sky at night."
}