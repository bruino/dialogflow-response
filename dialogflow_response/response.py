from typing import List
import json


class FulfillmentResponse:
    def __init__(self, fulfillment_text: str):
        self.fulfillment_text = fulfillment_text
        self._fulfillment_messages = None
        self._output_contexts = None
        self._followup_event_input = None

    def set_fulfillment_messages(self, messages: "List of Response Message"):
        self._fulfillment_messages = messages

    @staticmethod
    def context_factory(name: str, lifespan_count: int, parameters: dict) -> dict:
        return {
            "name": name,
            "lifespanCount": lifespan_count,
            "parameters": parameters,
        }

    def set_output_contexts(
        self, project_id: str, session: str, contexts: "List of context"
    ):
        _output_contexts = []
        for context in contexts:
            _output_contexts.append(
                {
                    "name": "projects/{}/agent/sessions/{}/contexts/{}".format(
                        project_id, session, context["name"]
                    ),
                    "lifespanCount": context["lifespanCount"],
                    "parameters": context["parameters"],
                }
            )
        self._output_contexts = _output_contexts

    def set_followup_event_input(self, name: str, parameters: dict):
        self._followup_event_input = {"name": name, "parameters": parameters}

    def as_dict(self) -> dict:
        fulfillment_response = dict()
        fulfillment_response["fulfillmentText"] = self.fulfillment_text

        if self._fulfillment_messages:
            fulfillment_response["fulfillmentMessages"] = self._fulfillment_messages

        if self._output_contexts:
            fulfillment_response["outputContexts"] = self._output_contexts

        if self._followup_event_input:
            fulfillment_response["followupEventInput"] = self._followup_event_input

        return fulfillment_response

    def as_json(self) -> str:
        return json.dumps(self.as_dict())


class SimpleResponse:
    def __init__(self, text: str, speak: str = None):
        self.text = text
        self.speak = speak
        self._plataforms = {
            "TELEGRAM": "for_telegram",
            "FACEBOOK": "for_facebook",
            "ACTIONS_ON_GOOGLE": "for_aog",
        }

    def for_plataform(self, plataform: str):
        if not plataform in self._plataforms:
            raise Exception("Not plataform exist.")
        return getattr(self, self._plataforms[plataform])()

    # TODO: support for multiple simple response.
    def for_aog(self) -> dict:
        return {
            "platform": "ACTIONS_ON_GOOGLE",
            "simpleResponses": {
                "simpleResponses": [
                    {
                        "displayText": self.text,
                        "textToSpeech": self.speak if self.speak else self.text,
                    }
                ]
            },
        }

    def for_facebook(self) -> dict:
        return {
            "platform": "FACEBOOK",
            "text": {
                "text": [self.text],
            },
        }

    def for_telegram(self) -> dict:
        return {
            "platform": "TELEGRAM",
            "text": {
                "text": [self.text],
            },
        }


class ChoicesResponse:
    def __init__(self, title: str, choices: List[str]):
        if len(title) == 0:
            raise Exception("Title is required.")
        if len(choices) <= 1:
            Exception("Choices response must contain at least on text string.")

        self.title = title
        self.choices = choices
        self._plataforms = {
            "TELEGRAM": "for_telegram",
            "FACEBOOK": "for_facebook",
            "ACTIONS_ON_GOOGLE": "for_aog",
        }

    def for_plataform(self, plataform: str):
        if not plataform in self._plataforms:
            raise Exception("Not plataform exist.")
        return getattr(self, self._plataforms[plataform])()

    def for_aog(self) -> dict:
        return {
            "platform": "ACTIONS_ON_GOOGLE",
            "payload": {
                "google": {
                    "expectUserResponse": True,
                    "richResponse": {
                        "items": [{"simpleResponse": {"textToSpeech": self.title}}],
                        "suggestions": [{"title": choice} for choice in self.choices],
                    },
                }
            },
        }

    def for_facebook(self) -> dict:
        return {
            "platform": "FACEBOOK",
            "quickReplies": {
                "title": self.title,
                "quickReplies": self.choices,
            },
        }

    # TODO: opciones de inline(aparece junto al msj) o keyboard(reemplaza al teclado)
    def for_telegram(self) -> dict:  # Keyboard for default.
        return {
            "platform": "TELEGRAM",
            "quickReplies": {
                "title": self.title,
                "quickReplies": self.choices,
            },
        }


class CardResponse:
    # TODO: ver enlace adjunto para no meter la pata
    # https://developers.google.com/assistant/conversational/df-asdk/rich-responses
    def __init__(
        self,
        title: str = None,
        subtitle: str = None,
        formatted_text: str = None,
        image: str = None,
        buttons: "List of [title_button, url_link]" = None,
    ):
        if not formatted_text and not image:
            raise Exception("Formatted text or image required.")

        if buttons and not title:
            raise Exception("Title is required for show buttons.")

        self.title = title
        self.subtitle = subtitle
        self.formatted_text = formatted_text
        self.image = image
        self.buttons = buttons
        self._plataforms = {
            "TELEGRAM": "for_telegram",
            "FACEBOOK": "for_facebook",
            "ACTIONS_ON_GOOGLE": "for_aog",
        }

    def for_plataform(self, plataform: str):
        if not plataform in self._plataforms:
            raise Exception("Not plataform exist.")
        return getattr(self, self._plataforms[plataform])()

    def for_aog(self) -> dict:
        image = None
        if self.image:  # "accessibilityText": image[1] TODO: pendiente de analizar
            image = {"imageUri": self.image}

        buttons = None
        if self.buttons:
            buttons = [
                {
                    "title": button[0],
                    "openUriAction": {
                        "uri": button[1],
                    },
                }
                for button in self.buttons
            ]

        basic_card = dict()
        basic_card["title"] = self.title
        basic_card["subtitle"] = self.subtitle or ""
        basic_card["formattedText"] = self.formatted_text or ""
        basic_card["buttons"] = buttons or []
        basic_card["image"] = image or None

        return {
            "platform": "ACTIONS_ON_GOOGLE",
            "basicCard": basic_card,
        }

    # TODO:?? corregir para que acepte todos los parámetros anteriores, seguramente recurra al payload
    def for_facebook(self) -> dict:
        buttons = None
        if self.buttons:
            buttons = [
                {"text": button[0], "postback": button[1]} for button in self.buttons
            ]

        subtitle = None
        if self.subtitle:
            subtitle = "%s \n%s" % (self.subtitle, self.formatted_text or "")

        card = dict()
        card["title"] = self.title
        card["subtitle"] = subtitle
        card["imageUri"] = self.image if self.image else None
        card["buttons"] = buttons or []

        return {
            "platform": "FACEBOOK",
            "card": card,
        }

    def for_telegram(self) -> dict:
        buttons = None
        if self.buttons:
            buttons = [
                {"text": button[0], "postback": button[1]} for button in self.buttons
            ]

        subtitle = None
        if self.subtitle:
            subtitle = "%s \n%s" % (self.subtitle, self.formatted_text or "")

        card = dict()
        card["title"] = self.title
        card["subtitle"] = subtitle
        card["imageUri"] = self.image if self.image else None
        card["buttons"] = buttons or []

        return {
            "platform": "TELEGRAM",
            "card": card,
        }


class ImageResponse:
    def __init__(self, url: str):
        if not url:
            raise Exception("URL in the image response is required.")

        self.url = url

    def for_aog(self) -> dict:
        return {
            "platform": "ACTIONS_ON_GOOGLE",
            "basicCard": {
                "image": {
                    "imageUri": self.url,
                }
            },
        }

    def for_facebook(self) -> dict:
        return {
            "platform": "FACEBOOK",
            "card": {
                "imageUri": self.url,
            },
        }

    def for_telegram(self) -> dict:
        return {
            "platform": "TELEGRAM",
            "card": {
                "imageUri": self.url,
            },
        }


class RequestLocationResponse:
    def __init__(self, text_message: str):
        self.text_message = text_message
        self._plataforms = {
            "TELEGRAM": "for_telegram",
            "ACTIONS_ON_GOOGLE": "for_aog",
        }

    def for_plataform(self, plataform: str):
        if not plataform in self._plataforms:
            raise Exception("Not plataform exist.")
        return getattr(self, self._plataforms[plataform])()

    def for_aog(self) -> dict:
        return {
            "platform": "ACTIONS_ON_GOOGLE",
            "payload": {
                "google": {
                    "expectUserResponse": True,
                    "systemIntent": {
                        "intent": "actions.intent.PERMISSION",
                        "data": {
                            "@type": "type.googleapis.com/google.actions.v2.PermissionValueSpec",
                            "optContext": self.text_message,
                            "permissions": ["NAME", "DEVICE_PRECISE_LOCATION"],
                        },
                    },
                }
            },
        }

    def for_telegram(self) -> dict:
        return {
            "platform": "TELEGRAM",
            "payload": {
                "telegram": {
                    "text": self.text_message,
                    "reply_markup": {
                        "keyboard": [
                            [{"text": "Send location 📍", "request_location": True}]
                        ]
                    },
                }
            },
        }


# TODO: Rich Response for Actions on Google.
# https://developers.google.com/assistant/conversational/df-asdk/rich-responses
# https://github.com/dialogflow/fulfillment-webhook-json/tree/master/responses/v2/ActionsOnGoogle/RichResponses
