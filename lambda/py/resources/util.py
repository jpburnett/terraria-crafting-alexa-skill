# -*- coding: utf-8 -*-
import random

from . import data
from typing import Dict

def load_locale_specific_recipe(locale):
    """
    Checks for a recipe dictionary with name 'RECIPE_<locale>' in data
    module and return it. Returns None if there is no dictionary
    specific to the locale.
    """
    
    ## type: (str) -> Dict[str, str]
    return getattr(data, "RECIPE_{}".format(locale).upper().replace("-", "_"), None)


def get_random_item(locale):
    """Return a random item from the locale specific dict."""
    ## type: (str) -> str
    return random.choice(list(load_locale_specific_recipe(locale).keys()))