import unittest
from dialogflow_response import RequestLocationResponse


class TestRequestLocationResponse(unittest.TestCase):
    def test_request_location_response_for_aog(self):
        self.assertEqual(
            RequestLocationResponse("To deliver your order").for_aog(),
            {
                "platform": "ACTIONS_ON_GOOGLE",
                "payload": {
                    "google": {
                        "expectUserResponse": True,
                        "systemIntent": {
                            "intent": "actions.intent.PERMISSION",
                            "data": {
                                "@type": "type.googleapis.com/google.actions.v2.PermissionValueSpec",
                                "optContext": "To deliver your order",
                                "permissions": ["NAME", "DEVICE_PRECISE_LOCATION"],
                            },
                        },
                    }
                },
            },
            "Not response correct.",
        )

    def test_request_location_response_for_telegram(self):
        self.assertEqual(
            RequestLocationResponse("To deliver your order").for_telegram(),
            {
                "platform": "TELEGRAM",
                "payload": {
                    "telegram": {
                        "text": "To deliver your order",
                        "reply_markup": {
                            "keyboard": [
                                [{"text": "Send location 📍", "request_location": True}]
                            ]
                        },
                    }
                },
            },
            "Not response correct.",
        )