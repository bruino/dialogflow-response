import unittest
from dialogflow_response import (
    FulfillmentResponse,
    SimpleResponse,
    CardResponse,
)


class TestFulfillmentResponse(unittest.TestCase):
    def test_fulfillment_text_response(self):
        self.assertEqual(
            FulfillmentResponse("Hello").as_dict(),
            {
                "fulfillmentText": "Hello",
            },
            "Not response correct.",
        )

    def test_fulfillment_response_with_fulfillment_messages(self):
        platform = "ACTIONS_ON_GOOGLE"
        response = FulfillmentResponse("Hello")
        response.set_fulfillment_messages(
            [
                SimpleResponse("Hello").for_platform(platform),
                CardResponse(
                    "title",
                    "subtitle",
                    "formatted text",
                    "image",
                    [
                        ["button 1", "link button 1"],
                        ["button 2", "link button 2"],
                    ],
                ).for_platform(platform),
            ]
        )
        self.assertEqual(
            response.as_dict(),
            {
                "fulfillmentText": "Hello",
                "fulfillmentMessages": [
                    {
                        "platform": "ACTIONS_ON_GOOGLE",
                        "simpleResponses": {
                            "simpleResponses": [
                                {
                                    "displayText": "Hello",
                                    "textToSpeech": "Hello",
                                }
                            ]
                        },
                    },
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
                ],
            },
            "Not response correct.",
        )

    def test_fulfillment_response_with_output_contexts(self):
        response = FulfillmentResponse("Hello")
        project_id = "project_foo_bar"
        session = "foo-bar"
        response.set_output_contexts(
            project_id,
            session,
            [
                FulfillmentResponse.context_factory(
                    "context.foo",
                    5,
                    {"param_1": "param_1 value", "param_2": "param_2 value"},
                ),
                FulfillmentResponse.context_factory(
                    "context.bar",
                    5,
                    {"param": "param value"},
                ),
            ],
        )

        self.assertEqual(
            response.as_dict(),
            {
                "fulfillmentText": "Hello",
                "outputContexts": [
                    {
                        "name": "projects/project_foo_bar/agent/sessions/foo-bar/contexts/context.foo",
                        "lifespanCount": 5,
                        "parameters": {
                            "param_1": "param_1 value",
                            "param_2": "param_2 value",
                        },
                    },
                    {
                        "name": "projects/project_foo_bar/agent/sessions/foo-bar/contexts/context.bar",
                        "lifespanCount": 5,
                        "parameters": {"param": "param value"},
                    },
                ],
            },
            "Not response correct.",
        )

    def test_fulfillment_response_full(self):
        platform = "TELEGRAM"
        response = FulfillmentResponse("Hello")
        response.set_fulfillment_messages(
            [
                SimpleResponse("Hello").for_platform(platform),
                CardResponse(
                    "title",
                    "subtitle",
                    "formatted text",
                    "image",
                    [
                        ["button 1", "link button 1"],
                        ["button 2", "link button 2"],
                    ],
                ).for_platform(platform),
            ]
        )
        response.set_output_contexts(
            "project_foo_bar",
            "foo-bar",
            [
                FulfillmentResponse.context_factory(
                    "context.foo",
                    5,
                    {"param": "param value"},
                ),
            ],
        )
        self.assertEqual(
            response.as_dict(),
            {
                "fulfillmentText": "Hello",
                "fulfillmentMessages": [
                    {
                        "platform": "TELEGRAM",
                        "text": {"text": ["Hello"]},
                    },
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
                ],
                "outputContexts": [
                    {
                        "name": "projects/project_foo_bar/agent/sessions/foo-bar/contexts/context.foo",
                        "lifespanCount": 5,
                        "parameters": {"param": "param value"},
                    },
                ],
            },
            "Not response correct.",
        )


"""
{
  "fulfillmentText": "This is a text response",
  "fulfillmentMessages": [
    {
      "card": {
        "title": "card title",
        "subtitle": "card text",
        "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
        "buttons": [
          {
            "text": "button text",
            "postback": "https://assistant.google.com/"
          }
        ]
      }
    }
  ],
  "source": "example.com",
  "payload": {
    "google": {
      "expectUserResponse": true,
      "richResponse": {
        "items": [
          {
            "simpleResponse": {
              "textToSpeech": "this is a simple response"
            }
          }
        ]
      }
    },
    "facebook": {
      "text": "Hello, Facebook!"
    },
    "slack": {
      "text": "This is a text response for Slack."
    }
  },
  "outputContexts": [
    {
      "name": "projects/${PROJECT_ID}/agent/sessions/${SESSION_ID}/contexts/context name",
      "lifespanCount": 5,
      "parameters": {
        "param": "param value"
      }
    }
  ],
  "followupEventInput": {
    "name": "event name",
    "languageCode": "en-US",
    "parameters": {
      "param": "param value"
    }
  }
}
"""
