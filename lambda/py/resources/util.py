# -*- coding: utf-8 -*-
import random

from . import data
from typing import Dict

def get_random_item():
    """Return a random item from the locale specific dict."""
    ## type: (str) -> str
    return random.choice(list(data.ITEMS.keys()))