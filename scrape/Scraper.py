import sys
sys.path.append("..") # Adds higher directory to python modules path.
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import config
import time

# Fetches payload from our specified MLH hackathon events URL


__author__="Jake Harwood"
__license__ = "MIT"


class Scraper:

    def __init__(self):
        self.data = self.__loadDriver()

    def __loadDriver(self):
        if config.WEB_DRIVER == config.BrowserType.FIREFOX:
            browser = webdriver.Firefox()
            browser.maximize_window()
        elif config.WEB_DRIVER == config.BrowserType.CHROME:
            from selenium.webdriver.chrome.options import Options
            chrome_options = Options()
            chrome_options.add_argument("--kiosk")
            browser = webdriver.Chrome(chrome_options=chrome_options)
        else:
            raise ValueError("Web driver not loaded. System exiting.")
            sys.exit(1)

        return browser

    def killDriver(self):
        if self.data is not None:
            self.data.close()


    def __loadAJAX(self):
        SCROLL_PAUSE_TIME = 1.0

        # Get scroll height
        last_height = self.data.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.data.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.data.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height


    def getPayload(self):
        if self.data is not None:
            try:
                self.data.get(config.WEBPAGE_URL)
                self.data.get(config.REDIRECT_URL)

                self.__loadAJAX()

                if self.data.current_url != config.REDIRECT_URL:
                    self.killDriver()
                    raise ValueError("URL of web driver does not match the URL we want to scrape")
            except TimeoutException:
                self.killDriver()
                raise TimeoutException("GET Request on URL has timed out")

            return self.data.page_source

