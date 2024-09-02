# Telegram API_ID & API_HASH Getter

This script automates the process of obtaining your `API_ID` and `API_HASH` from Telegram using Selenium WebDriver. It requires ChromeDriver and the Chrome browser to work properly.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Chrome browser
- ChromeDriver (compatible with your version of Chrome)

## Installation

- open cmd
- git clone https://github.com/DonsPabloXYZ/telegram-get-api
- cd telegram-get-api
- pip install selenium colorama
- python main.py
- The script will save the obtained API_ID and API_HASH in a file named data.txt in the same directory as the script.

Download ChromeDriver:
Download ChromeDriver from [here](https://developer.chrome.com/docs/chromedriver/downloads) and place it in a directory on your system. Update the CHROME_DRIVER_PATH in the script to point to the location of your chromedriver.exe.

Configuration
Update ChromeDriver Path:
Open the script file and update the CHROME_DRIVER_PATH variable with the path to your chromedriver.exe:
CHROME_DRIVER_PATH = "path/to/your/chromedriver.exe"

Output
The script will save the obtained API_ID and API_HASH in a file named data.txt in the same directory as the script.

Troubleshooting
Ensure that ChromeDriver and Chrome browser versions are compatible.
If you encounter issues with element locators, inspect the Telegram web page for changes and update the script accordingly.
Ensure that your phone number and OTP are correctly entered.
