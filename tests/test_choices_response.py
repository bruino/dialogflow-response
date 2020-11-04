import unittest
from dialogflow_response import ChoicesResponse


class TestChoicesResponse(unittest.TestCase):
    def test_choises_response_for_aog(self):
        self.assertEqual(
            ChoicesResponse("Select one color:", ["Red", "Blue", "Yellow"]).for_aog(),
            {
                "platform": "ACTIONS_ON_GOOGLE",
                "payload": {
                    "google": {
                        "expectUserResponse": True,
                        "richResponse": {
                            "items": [
                                {
                                    "simpleResponse": {
                                        "textToSpeech": "Select one color:",
                                    }
                                },
                            ],
                            "suggestions": [
                                {"title": "Red"},
                                {"title": "Blue"},
                                {"title": "Yellow"},
                            ],
                        },
                    }
                },
            },
            "Not response correct.",
        )

    def test_choises_response_for_facebook(self):
        self.assertEqual(
            ChoicesResponse(
                "Select one color:", ["Red", "Blue", "Yellow"]
            ).for_facebook(),
            {
                "platform": "FACEBOOK",
                "quickReplies": {
                    "title": "Select one color:",
                    "quickReplies": ["Red", "Blue", "Yellow"],
                },
            },
            "Not response correct.",
        )

    def test_choises_response_for_telegram(self):
        self.assertEqual(
            ChoicesResponse(
                "Select one color:", ["Red", "Blue", "Yellow"]
            ).for_telegram(),
            {
                "platform": "TELEGRAM",
                "quickReplies": {
                    "title": "Select one color:",
                    "quickReplies": ["Red", "Blue", "Yellow"],
                },
            },
            "Not response correct.",
        )