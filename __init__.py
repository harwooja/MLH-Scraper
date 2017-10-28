import config
from scrape.Scraper import Scraper
from parse.Parser import Parse

__author__ = "Jake Harwood"
__license__ = "MIT"


class Run:

    def __init__(self):
        self.scrapeData = Scraper()
        if self.scrapeData is not None:
            webpagePayload = self.scrapeData.getPayload()
            self.parser = Parse(webpagePayload)
            self.parser.getEventMap()
            self.__cleanup()
        else:
            raise TypeError("Error: Invalid Payload")

    def __cleanup(self):
        self.scrapeData.killDriver()


Run()
