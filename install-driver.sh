#!/bin/bash

printf "Welcome to the driver installer. This script will install the appropriate web driver for the selenium framework. \n\n"

while [ true ];
do
	echo "Enter browser (character only): For Chrome 'C', Firefox 'F' : "
	read BROWSER
	if [ $BROWSER == "C" ] || [ $BROWSER == "F" ]
	then
		break
	else 
		printf "Incorrect input. Please try again \n\n"
	fi
done

OSTYPE=$(uname)
# Chrome Linux
chrome_linux="https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip"
# Chrome Mac OS
chrome_macos="https://chromedriver.storage.googleapis.com/2.33/chromedriver_mac64.zip"
# Firefox Linux
firefox_linux="https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-linux64.tar.gz"
#Firefox OSX
firefox_macos="https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-macos.tar.gz"

# File path
driver="/usr/local/sbin/driver"


function driverFailure() {
    echo "Error: Web driver did not install correctly"
    exit
}

printf "\n\n Now installing the appropriate web driver...\n\n"

if [ $OSTYPE == "Linux" ]
then
	if [ $BROWSER == "C" ]
	then
		curl -o $driver $chrome_linux && unzip $driver -d /usr/local/sbin && rm $driver
	elif [ $OSTYPE == "F" ]
	then
		curl -0L -o $driver $firefox_linux && tar -xf $driver -C /usr/local/sbin && rm $driver
	else
	    driverFailure
	fi
elif [ $OSTYPE == "Darwin" ]
then
	if [ $BROWSER == "C" ]
	then
		curl -o $driver $chrome_macos && unzip $driver -d /usr/local/sbin && rm $driver
	elif [ $OSTYPE == "F" ]
	then
		curl -0L -o $driver $firefox_macos && tar -xf $driver -C /usr/local/sbin && rm $driver
	else
	    driverFailure
	fi
else
    echo "Operating System Type is not compatible."
    exit
fi


printf "Updating \$PATH to contain driver path /usr/local/sbin \n\n"
echo "export PATH=$PATH:/usr/local/sbin" >> ~/.bashrc

echo "Driver installation complete"









