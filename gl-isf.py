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

def progress_bar(num_processing, num_games, eta):
    percentage = num_processing / num_games * 100
    percentage_str = round(percentage, 1)
    # if last_tt == 0:
    #     eta = "~"
    # else:
    #     eta = round(((num_games - num_processing) * last_tt) / 60, 2)
    #     eta_avg = round(((num_games - num_processing) * (time_sum / num_processing)) / 60, 2)
    # stat_counter = f" [{Fore.GREEN}{num_processing}{Style.RESET_ALL}/{Style.BRIGHT}{Fore.YELLOW}{num_games}{Style.RESET_ALL} {Style.BRIGHT}{percentage_str}%{Style.RESET_ALL} - {Style.BRIGHT}{eta}m{Style.RESET_ALL} left] "
    stat_counter = f" [{Fore.GREEN}{num_processing}{Style.RESET_ALL}/{Style.BRIGHT}{Fore.YELLOW}{num_games}{Style.RESET_ALL} {Style.BRIGHT}{percentage_str}%{Style.RESET_ALL} - {Style.BRIGHT}{eta}{Style.RESET_ALL} left] "
    # stat_counter = stat_counter_str.ljust(65)
    if percentage >= 0 and percentage < 5:
        return(f"[{Fore.GREEN}.         {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 5 and percentage < 10:
        return(f"[{Fore.GREEN}:         {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 10 and percentage < 15:
        return(f"[{Fore.GREEN}:.        {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 15 and percentage < 20:
        return(f"[{Fore.GREEN}::        {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 20 and percentage < 25:
        return(f"[{Fore.GREEN}::.       {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 25 and percentage < 30:
        return(f"[{Fore.GREEN}:::       {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 30 and percentage < 35:
        return(f"[{Fore.GREEN}:::{Fore.YELLOW}.      {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 35 and percentage < 40:
        return(f"[{Fore.GREEN}:::{Fore.YELLOW}:      {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 40 and percentage < 45:
        return(f"[{Fore.GREEN}:::{Fore.YELLOW}:.     {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 45 and percentage < 50:
        return(f"[{Fore.GREEN}:::{Fore.YELLOW}::     {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 50 and percentage < 55:
        return(f"[{Fore.GREEN}:::{Fore.YELLOW}::.    {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 55 and percentage < 60:
        return(f"[{Fore.GREEN}:::{Fore.YELLOW}:::    {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 60 and percentage < 65:
        return(f"[{Fore.GREEN}:::{Fore.YELLOW}:::.   {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 65 and percentage < 70:
        return(f"[{Fore.GREEN}:::{Fore.YELLOW}::::   {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 70 and percentage < 75:
        return(f"[{Fore.GREEN}:::{Fore.YELLOW}::::{Fore.RED}.  {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 75 and percentage < 80:
        return(f"[{Fore.GREEN}:::{Fore.YELLOW}::::{Fore.RED}:  {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 80 and percentage < 85:
        return(f"[{Fore.GREEN}:::{Fore.YELLOW}::::{Fore.RED}:. {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 85 and percentage < 90:
        return(f"[{Fore.GREEN}:::{Fore.YELLOW}::::{Fore.RED}:: {Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 90 and percentage < 95:
        return(f"[{Fore.GREEN}:::{Fore.YELLOW}::::{Fore.RED}::.{Style.RESET_ALL}]{stat_counter}")
    elif percentage >= 95 and percentage <= 100:
        return(f"[{Fore.GREEN}:::{Fore.YELLOW}::::{Fore.RED}:::{Style.RESET_ALL}]{stat_counter}")