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

        card_title = _(data.DISPLAY_CARD_TITLE).format(
            _(data.SKILL_NAME), item_name)

        my_recipes = data.ITEMS

        if item_name in my_recipes:
            recipe = my_recipes[item_name]
            # session_attributes['speech'] = recipe
            handler_input.response_builder.speak(recipe).set_card(
                SimpleCard(card_title, recipe))
        else:
            speech = _(data.RECIPE_NOT_FOUND_MESSAGE)
            reprompt = _(data.RECIPE_NOT_FOUND_REPROMPT)
            if item_name:
                speech += _(data.RECIPE_NOT_FOUND_WITH_ITEM_NAME).format(
                    item_name)
            else:
                speech += _(data.RECIPE_NOT_FOUND_WITHOUT_ITEM_NAME)
            speech += reprompt

            handler_input.response_builder.speak(speech).ask(
                reprompt)

        return handler_input.response_builder.response

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

        # Create Card
        card_title = "Random Item"
        card_text = "test"
        speech_text = "Hello there"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard(card_title, card_text)
        ) 

        return handler_input.response_builder.response

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]

        item = util.get_random_item()

        speech = _(data.HELP_MESSAGE).format(item)

        handler_input.response_builder.speak(speech).ask(speech)
        return handler_input.response_builder.response


class RepeatIntentHandler(AbstractRequestHandler):
    """Handler for Repeat Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.RepeatIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In RepeatIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]

        session_attributes = handler_input.attributes_manager.session_attributes
        handler_input.response_builder.speak(
            session_attributes['speech']).ask(
            session_attributes['reprompt'])
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Handler for Cancel and Stop Intents."""
    def can_handle(self, handler_input):
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelOrStopIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]

        speech = _(data.STOP_MESSAGE).format(_(data.SKILL_NAME))
        handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for Fallback Intent.
    AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]

        item = util.get_random_item()

        help_message = _(data.HELP_MESSAGE).format(item)
        help_reprompt = _(data.HELP_REPROMPT).format(item)
        speech = _(data.FALLBACK_MESSAGE).format(
            _(data.SKILL_NAME)) + help_message
        reprompt = _(data.FALLBACK_MESSAGE).format(
            _(data.SKILL_NAME)) + help_reprompt

        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for SessionEndedRequest."""
    def can_handle(self, handler_input):
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")
        logger.info("Session ended with reason: {}".format(
            handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Global exception handler."""
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        logger.error(exception, exc_info=True)
        logger.info("Original request was {}".format(
            handler_input.request_envelope.request))

        speech = _("Sorry, I can't understand the command. Please say again!!")
        handler_input.response_builder.speak(speech).ask(speech)

        return handler_input.response_builder.response


class CacheSpeechForRepeatInterceptor(AbstractResponseInterceptor):
    """Cache the output speech and reprompt to session attributes,
    for repeat intent.
    """
    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        session_attr = handler_input.attributes_manager.session_attributes
        session_attr["speech"] = response.output_speech
        session_attr["reprompt"] = response.reprompt


class LocalizationInterceptor(AbstractRequestInterceptor):
    """Add function to request attributes, that can load locale specific data."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        locale = handler_input.request_envelope.request.locale
        logger.info("Locale is {}".format(locale))
        i18n = gettext.translation(
            'data', localedir='locales', languages=[locale], fallback=True)
        handler_input.attributes_manager.request_attributes["_"] = i18n.gettext


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