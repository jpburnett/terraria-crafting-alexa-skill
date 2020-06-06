"""
Skill to help with crafting options in Terraria
"""
#--------------------------------------------------------------------------
# Python Libraries
#--------------------------------------------------------------------------
import logging
import gettext

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
# Resource Libraries
#--------------------------------------------------------------------------
from resources import data, util
from skill import HelpIntentHandler, CancelOrStopIntentHandler, RepeatIntentHandler, \
    FallbackIntentHandler, SessionEndedRequestHandler, CatchAllExceptionHandler, \
    CacheSpeechForRepeatInterceptor, LocalizationInterceptor
from skill import RandomItemIntentHandler

# Set Logging 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#--------------------------------------------------------------------------
# Handlers
#--------------------------------------------------------------------------
class LaunchRequestHandler(AbstractRequestHandler):
    """
    Handler for skill launch.

    Parameters:
    AbstractRequestHandler (obj): Amazon Request Handler object

    Returns: Amazon response object
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In LaunchRequestHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]

        item = util.get_random_item()
        speech = _(data.WELCOME_MESSAGE).format(
            _(data.SKILL_NAME), item)

        reprompt = _(data.WELCOME_REPROMPT)

        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(data.SKILL_NAME, "Terraria Tool")
        ).ask(reprompt)

        return handler_input.response_builder.response


class RecipeIntentHandler(AbstractRequestHandler):
    """
    Handler for getting the recipe for an item

    Parameters:
    AbstractRequestHandler (obj): Amazon Request Handler object

    Returns: Amazon request with the item the user requested
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("RecipeIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In RecipeIntentHandler")

        _ = handler_input.attributes_manager.request_attributes["_"]

        try:
            item_name = handler_input.request_envelope.request.intent.slots["Item"].value.lower()
        except AttributeError:
            logger.info("Could not resolve item name")
            item_name = None

        card_title = _(data.DISPLAY_CARD_TITLE).format(_(data.SKILL_NAME), item_name)

        list_of_items = data.ITEMS

        # I was dumb and didn't put all 3000 items as lowercase...so here we are
        #TODO: Eventually fix the dictionary, but get this working first
        list_of_items = {k.lower(): v for k, v in list_of_items.items()}

        if item_name in list_of_items:
            recipe = list_of_items[item_name]
            # session_attributes['speech'] = recipe
            handler_input.response_builder.speak(recipe).set_card(
                SimpleCard(card_title, recipe)).set_should_end_session(True)
        else:
            speech = _(data.ITEM_NOT_FOUND_MESSAGE)
            reprompt = _(data.ITEM_NOT_FOUND_REPROMPT)
            if item_name:
                speech += _(data.ITEM_NOT_FOUND_WITH_ITEM_NAME).format(
                    item_name)
            else:
                speech += _(data.ITEM_NOT_FOUND_WITHOUT_ITEM_NAME)
            speech += reprompt

            handler_input.response_builder.speak(speech).ask(
                reprompt)

        #TODO: Is there a way to put in here "would you like to know another item" 
        # instead of having to open the skill multiple times?

        return handler_input.response_builder.response


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(RecipeIntentHandler())
sb.add_request_handler(RandomItemIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(RepeatIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

sb.add_global_request_interceptor(LocalizationInterceptor())
sb.add_global_response_interceptor(CacheSpeechForRepeatInterceptor())

lambda_handler = sb.lambda_handler()