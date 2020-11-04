import unittest
from dialogflow_response import ImageResponse


class TestImageResponse(unittest.TestCase):
    def test_image_response_for_aog(self):
        self.assertEqual(
            ImageResponse("image").for_aog(),
            {
                "platform": "ACTIONS_ON_GOOGLE",
                "basicCard": {
                    "image": {
                        "imageUri": "image",
                    },
                },
            },
            "Not response correct.",
        )

    def test_image_response_for_facebook(self):
        self.assertEqual(
            ImageResponse("image").for_facebook(),
            {
                "platform": "FACEBOOK",
                "card": {
                    "imageUri": "image",
                },
            },
            "Not response correct.",
        )

    def test_image_response_for_telegram(self):
        self.assertEqual(
            ImageResponse("image").for_telegram(),
            {
                "platform": "TELEGRAM",
                "card": {
                    "imageUri": "image",
                },
            },
            "Not response correct.",
        )
