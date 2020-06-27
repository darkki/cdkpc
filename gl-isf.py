from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import urllib.request
import requests

import datetime
date_time_now = datetime.datetime.now()
import time

from colorama import init # module imported for color support
init()
from colorama import Fore,Back,Style

class app_info:
    name = "GameList-import.scrape.format"
    version = "20200623|Dev"
    by = "darkk!"

def time_convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    if int(hour) == 0 and int(minutes) == 0 and int(seconds) == 0:
        return("~")
    elif int(hour) == 0 and int(minutes) == 0:
        return(f"{int(seconds)}s")
    elif int(hour) == 0:
        return(f"{int(minutes)}m {int(seconds)}s")
    else:
        return(f"{int(hour)}h {int(minutes)}m {int(seconds)}s")