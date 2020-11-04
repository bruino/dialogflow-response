import unittest
from dialogflow_response import SimpleResponse


class TestSimpleResponse(unittest.TestCase):
    def test_simple_response_text_for_aog(self):
        self.assertEqual(
            SimpleResponse("Foo bar").for_aog(),
            {
                "platform": "ACTIONS_ON_GOOGLE",
                "simpleResponses": {
                    "simpleResponses": [
                        {
                            "displayText": "Foo bar",
                            "textToSpeech": "Foo bar",
                        }
                    ]
                },
            },
            "Not response correct.",
        )

    def test_simple_response_text_and_speak_for_aog(self):
        self.assertEqual(
            SimpleResponse("Foo bar", "Foo").for_aog(),
            {
                "platform": "ACTIONS_ON_GOOGLE",
                "simpleResponses": {
                    "simpleResponses": [
                        {
                            "displayText": "Foo bar",
                            "textToSpeech": "Foo",
                        }
                    ]
                },
            },
            "Not response correct.",
        )

    def test_simple_response_text_for_facebook(self):
        self.assertEqual(
            SimpleResponse("Hello world").for_facebook(),
            {
                "platform": "FACEBOOK",
                "text": {"text": ["Hello world"]},
            },
            "Not response correct.",
        )

    def test_simple_response_text_for_telegram(self):
        self.assertEqual(
            SimpleResponse("Hello world").for_telegram(),
            {
                "platform": "TELEGRAM",
                "text": {"text": ["Hello world"]},
            },
            "Not response correct.",
        )