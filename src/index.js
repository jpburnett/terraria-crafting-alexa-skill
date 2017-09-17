/**
 * This Skill demonstrates how to craft certain items in the computer game Terraria
 * This supports multiple languages (en-US, en-GB, more to come soon, I know there isn't any difference between the english).
 * The Intents, Slot and Sample Utterances for this skill, as well as the code
 * and instructions are located at https://github.com/jpburnett/terraria-tool-skill
 **/

'use strict';

const Alexa = require('alexa-sdk');
const recipes = require('./recipes');

const APP_ID = "amzn1.ask.skill.aef9004a-f2bc-42a6-bd57-d01742f264e5";

const languageStrings = {
    'en': {
        translation: {
            RECIPES: recipes.RECIPE_EN_US,
            SKILL_NAME: 'Terraria Tool',
            WELCOME_MESSAGE: "Welcome to %s. You can ask a question like, what\'s the recipe for a torch? ... Now, how may I help you?",
            WELCOME_REPROMPT: 'For instructions on what you can say, please say help me.',
            DISPLAY_CARD_TITLE: '%s  - Recipe for %s.',
            HELP_MESSAGE: "You can ask questions such as, what\'s the recipe, or, you can say exit...Now, how may I help you?",
            HELP_REPROMPT: "You can say things like, what\'s the recipe, or you can say exit...Now, how may I help you?",
            STOP_MESSAGE: 'Happy Crafting!',
            RECIPE_REPEAT_MESSAGE: 'Try saying repeat.',
            RECIPE_NOT_FOUND_MESSAGE: "I\'m sorry, I don\'t know that recipe yet.",
            RECIPE_NOT_FOUND_WITH_ITEM_NAME: 'the recipe for %s. ',
            RECIPE_NOT_FOUND_WITHOUT_ITEM_NAME: 'that recipe. ',
            RECIPE_NOT_FOUND_REPROMPT: 'Is there anything else that I can help help with?',
        },
    },
    'en-US': {
        translation: {
            RECIPES: recipes.RECIPE_EN_US,
            SKILL_NAME: 'Terraria Tool',
        },
    },
    'en-GB': {
        translation: {
            RECIPES: recipes.RECIPE_EN_GB,
            SKILL_NAME: 'Terraria Tool',
        },
    },
};

var handlers = {
    'LaunchRequest': function () {
        this.attributes.speechOutput = this.t('WELCOME_MESSAGE', this.t('SKILL_NAME'));
        // If the user does not reply to the welcome message or says something that is not understood, they will be prompted again with this text.
        this.attributes.repromptSpeech = this.t('WELCOME_REPROMPT');
        this.response.speak(this.attributes.speechOutput).listen(this.attributes.repromptSpeech);
        this.emit(':responseReady');
    },
    'RecipeIntent': function () {
        const itemSlot = this.event.request.intent.slots.Item;
        let itemName;
        if (itemSlot && itemSlot.value) {
            itemName = itemSlot.value.toLowerCase();
        }

        const cardTitle = this.t('DISPLAY_CARD_TITLE', this.t('SKILL_NAME'), itemName);
        const myRecipes = this.t('RECIPES');
        const recipe = myRecipes[itemName];

        if (recipe) {
            this.attributes.speechOutput = recipe;
            this.attributes.repromptSpeech = this.t('RECIPE_REPEAT_MESSAGE');

            this.response.speak(recipe).listen(this.attributes.repromptSpeech);
            this.response.cardRenderer(cardTitle, recipe);
            this.emit(':responseReady');
        } else {
            let speechOutput = this.t('RECIPE_NOT_FOUND_MESSAGE');
            const repromptSpeech = this.t('RECIPE_NOT_FOUND_REPROMPT');
            if (itemName) {
                speechOutput += this.t('RECIPE_NOT_FOUND_WITH_ITEM_NAME', itemName);
            } else {
                speechOutput += this.t('RECIPE_NOT_FOUND_WITHOUT_ITEM_NAME');
            }
            speechOutput += repromptSpeech;

            this.attributes.speechOutput = speechOutput;
            this.attributes.repromptSpeech = repromptSpeech;

            this.response.speak(speechOutput).listen(repromptSpeech);
            this.emit(':responseReady');
        }
    },
    'AMAZON.HelpIntent': function () {
        this.response.speak(this.t('HELP')).listen(this.t('HELP'))
        this.attributes.speechOutput = this.t('HELP_MESSAGE');
        this.attributes.repromptSpeech = this.t('HELP_REPROMPT');
        this.response.speak(this.attributes.speechOutput).listen(this.attributes.repromptSpeech);
        this.emit(':responseReady');
    },
    'AMAZON.RepeatIntent': function () {
        this.response.speak(this.attributes.speechOutput).listen(this.attributes.repromptSpeech);
        this.emit(':responseReady');
    },
    'AMAZON.StopIntent': function () {
        this.emit('SessionEndedRequest');
    },
    'AMAZON.CancelIntent': function () {
        this.response.speak(this.t('STOPING'));
        this.emit('SessionEndedRequest');
    },
    'SessionEndedRequest': function () {
        this.response.speak(this.t('STOP_MESSAGE'));
        this.emit(':responseReady');
    },
    'Unhandled': function () {
        this.attributes.speechOutput = this.t('HELP_MESSAGE');
        this.attributes.repromptSpeech = this.t('HELP_REPROMPT');
        this.response.speak(this.attributes.speechOutput).listen(this.attributes.repromptSpeech);
        this.emit(':responseReady');
    },
};

exports.handler = function (event, context) {
    var alexa = Alexa.handler(event, context);
    alexa.APP_ID = APP_ID;
    // To enable string internationalization (i18n) features
    alexa.resources = languageStrings;
    alexa.registerHandlers(handlers);
    alexa.execute();
};
