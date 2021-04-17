# Dialogflow Response

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Build Status](https://travis-ci.com/bruino/dialogflow-response.svg?branch=master)](https://travis-ci.com/bruino/dialogflow-response)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Easily implement Dialogflow's fulfillment webhook responses for v2 agents with this small library in python.

Supported features:
- Text
- Card
- Image
- Suggestion Chips (Quick Replies)
- Request Location

Supported 3 chat platforms: [Actions On Google](https://developers.google.com/assistant), [Facebook Messenger](https://www.messenger.com/) and [Telegram](https://telegram.org/).

## Test
Inside directory, run tests:

```
python3 -m unittest discover
```