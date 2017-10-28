import sys
sys.path.append("..") # Adds higher directory to python modules path.
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import config

# Fetches payload from our specified MLH hackathon events URL


__author__="Jake Harwood"
__license__ = "MIT"


class Scraper:

    def __init__(self):
        self.data = self.__loadDriver()

    def __loadDriver(self):
        if config.WEB_DRIVER == config.BrowserType.FIREFOX:
            browser = webdriver.Firefox()
        elif config.WEB_DRIVER == config.BrowserType.CHROME:
            browser = webdriver.Chrome()
        else:
            raise ValueError("Web driver not loaded. System exiting.")
            sys.exit(1)

        return browser

    def killDriver(self):
        if self.data is not None:
            self.data.close()

    def getPayload(self):
        if self.data is not None:
            try:
                self.data.get(config.WEBPAGE_URL)
                self.data.get(config.REDIRECT_URL)

                if self.data.current_url != config.REDIRECT_URL:
                    self.killDriver()
                    raise ValueError("URL of web driver does not match the URL we want to scrape")
            except TimeoutException:
                self.killDriver()
                raise TimeoutException("GET Request on URL has timed out")

            return self.data.page_source

