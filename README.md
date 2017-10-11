# Prettify JSON

A simple program that pretty prints JSON from file.

# Quickstart

This script requires Python 3 to work.

Example of script launch on Linux, Python 3.5:

```#!bash

$ python pprint_json.py demo.json
{
    "widget": {
        "debug": "on",
        "image": {
            "alignment": "center",
            "hOffset": 250,
            "name": "sun1",
            "src": "Images/Sun.png",
            "vOffset": 250
        },
        "text": {
            "alignment": "center",
            "data": "Click Here",
            "hOffset": 250,
            "name": "text1",
            "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;",
            "size": 36,
            "style": "bold",
            "vOffset": 100
        },
        "window": {
            "height": 500,
            "name": "main_window",
            "title": "Sample Konfabulator Widget",
            "width": 500
        }
    }
}

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
