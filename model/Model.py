class HackathonModel:

    def __init__(self, hackathonName, location, url, date):
        self.hackathonName = hackathonName
        self.location = location
        self.url = url
        self.date = date


    def getName(self):
        return self.hackathonName

    def getLocation(self):
        return self.location

    def url(self):
        return self.url

    def date(self):
        return self.date