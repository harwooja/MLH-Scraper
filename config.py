from enum import Enum
import urllib.parse


# Configuration file for MLH-Scraper

__author__="Jake Harwood"
__license__ = "MIT"


class BrowserType(Enum):
    FIREFOX = "FIREFOX"
    CHROME = "CHROME"

# URL of MLH Hackathon Events Page
WEBPAGE_URL = "https://mlh.io/beta/events/on"
REDIRECT_URL = "https://mlh.io/beta/events?utf8=%E2%9C%93&search%5Bregion%5D=North+America&search%5Bname%5D=&search%5Bpast_events%5D=on"

# DRIVER ["CHROME" or "FIREFOX"]
WEB_DRIVER = BrowserType.CHROME



