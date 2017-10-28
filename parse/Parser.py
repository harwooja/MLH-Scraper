import sys
sys.path.append("..") # Adds higher directory to python modules path.
from bs4 import BeautifulSoup
from model import Model

# Parses web payload that is retrieved from the Scraper module


__author__="Jake Harwood"
__license__ = "MIT"


class Parse:

    def __init__(self, data):
        self.data = BeautifulSoup(data, "lxml")
        self.eventMap = {}
        self.__parse()

    def __parse(self):

        hackathonItems = self.data.find("table", {"id": "events-table"}).find("tbody").find_all("tr")

        for hackathon in hackathonItems:
            hackathonName = hackathon.find("span", {"class": "event-title"}).get_text()
            hackathonLocation = hackathon.find("td", {"class": "event-location"}).find("a", {"class": "event-link"}).getText()
            hackathonUrl = hackathon.find("td", {"class": "event-website"}).find("a", {"class": "event-link"})['href']
            hackathonDate = hackathon.find("td", {"class": "event-date"}).find("a", {"class": "event-link"}).getText()
            self.eventMap[hackathonName] = Model.HackathonModel(hackathonName, hackathonLocation, hackathonUrl, hackathonDate)

    def getEventMap(self):
        if self.eventMap is not None:
            return self.eventMap

    def getPrettyPayload(self):
        if self.data is not None:
            return self.data.prettify()

