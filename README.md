# MLH-Scraper (Event Scraper)

## What is MLH-Scraper?

It's a web-scraper and parser implemented in python for all Hackathon event's within the [Major League Hacking](https://mlh.io/) circuit.

## Who is MLH-Scraper for?

Anyone who needs all Hackathon events (event name, location, website, and date) for the yearly circuit (example: 2017-2018)


## Dependencies

* Python 3
* Pip
* Bash
* Either Chrome or Firefox

MLH-Scraper uses [Selenium](http://www.seleniumhq.org/). It loads a process instance of Chrome or Firefox (specified in the config.py file) and uses that to get the payload (page) data. 


## How do I run MLH-Scraper?

After you do configuration setup, simply run the \__init\__.py module and it will load a dictionary named "eventMap" with all Hackathon event data split into model objects named "HackathonModel". 

```python
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
```

## Configuration

1. Navigate with bash to the root directory of the project on your harddrive.
2. Run **make install-dependencies**. This will install all the Python3 dependencies as well as load a script that will download and install the Selenium web driver.
3. Run **\__init\__.py** to execute MLH-Scraper




### Tools used:

 * [Selenium](http://www.seleniumhq.org/)
 * [BeautifulSoup4](https://pypi.python.org/pypi/beautifulsoup4)
