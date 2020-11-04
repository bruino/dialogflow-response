import unittest
from dialogflow_response import CardResponse


class TestCardResponse(unittest.TestCase):
    def test_card_response_for_aog(self):
        self.assertEqual(
            CardResponse(
                "title",
                "subtitle",
                "formatted text",
                "image",
                [
                    ["button 1", "link button 1"],
                    ["button 2", "link button 2"],
                ],
            ).for_aog(),
            {
                "platform": "ACTIONS_ON_GOOGLE",
                "basicCard": {
                    "title": "title",
                    "subtitle": "subtitle",
                    "formattedText": "formatted text",
                    "buttons": [
                        {
                            "title": "button 1",
                            "openUriAction": {
                                "uri": "link button 1",
                            },
                        },
                        {
                            "title": "button 2",
                            "openUriAction": {
                                "uri": "link button 2",
                            },
                        },
                    ],
                    "image": {
                        "imageUri": "image",
                    },
                },
            },
            "Not response correct.",
        )

    def test_card_response_for_facebook(self):
        self.assertEqual(
            CardResponse(
                "title",
                "subtitle",
                "formatted text",
                "image",
                [
                    ["button 1", "link button 1"],
                    ["button 2", "link button 2"],
                ],
            ).for_facebook(),
            {
                "platform": "FACEBOOK",
                "card": {
                    "title": "title",
                    "subtitle": "subtitle \nformatted text",
                    "imageUri": "image",
                    "buttons": [
                        {
                            "text": "button 1",
                            "postback": "link button 1",
                        },
                        {
                            "text": "button 2",
                            "postback": "link button 2",
                        },
                    ],
                },
            },
            "Not response correct.",
        )

    def test_card_response_for_telegram(self):
        self.assertEqual(
            CardResponse(
                "title",
                "subtitle",
                "formatted text",
                "image",
                [
                    ["button 1", "link button 1"],
                    ["button 2", "link button 2"],
                ],
            ).for_telegram(),
            {
                "platform": "TELEGRAM",
                "card": {
                    "title": "title",
                    "subtitle": "subtitle \nformatted text",
                    "imageUri": "image",
                    "buttons": [
                        {
                            "text": "button 1",
                            "postback": "link button 1",
                        },
                        {
                            "text": "button 2",
                            "postback": "link button 2",
                        },
                    ],
                },
            },
            "Not response correct.",
        )