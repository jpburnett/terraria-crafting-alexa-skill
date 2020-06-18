"""
Filename: random_item_intent.py

Description: handles the random item intent
"""
#--------------------------------------------------------------------------
# AwS Libraries
#--------------------------------------------------------------------------
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractResponseInterceptor, AbstractRequestInterceptor)
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

#--------------------------------------------------------------------------
# Python Libraries
#--------------------------------------------------------------------------
import logging
import gettext

#--------------------------------------------------------------------------
# Resource Libraries
#--------------------------------------------------------------------------
from skill.resources import data, util

# Set Logging 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class RandomItemIntentHandler(AbstractRequestHandler):
    """
    Handler for getting the recipe for a random item.

    Parameters:
    AbstractRequestHandler (obj): Amazon Request Handler object

    Returns: amazon response object
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("RandomItemIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In RandomItemIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]

        list_of_items = data.ITEMS

        #Get the random item
        item = util.get_random_item()
        
        recipe = list_of_items[item]

        # Create Card
        card_title = _(data.DISPLAY_CARD_TITLE).format(_("Random Item"), item)

        speech_text = recipe

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard(card_title, recipe)
        ).set_should_end_session(True)

        return handler_input.response_builder.response