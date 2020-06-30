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

import argparse

class app_info:
    shortname = "GL-isf"
    name = "GameList-import.scrape.format"
    description = "imports, scrapes and formats your game list!"
    version = "20200627|Dev"
    by = "darkk!"

parser = argparse.ArgumentParser(prog=app_info.shortname, description=app_info.description)
parser.add_argument('input_filename", help="filename of gamelist to read [ formatting: "gamename -- steam_url" ]')
### parser.add_argument("input", nargs="?", type=argparse.FileType('r'), help="filename of gamelist to read", default="gamelist.glf")
parser.add_argument("-v", "--version", action="version", version="[GL-isf] GameList-import.scrape.format v" + app_info.version + " by " + app_info.by)
### parser.add_argument("-m", "--mono", help="output in monochrome (no colors)", action="store_false")
args = parser.parse_args()
### print(args.input_filename)

app_ascii = """
                      ________.____              .__         _____ 
                     /  _____/|    |             |__| ______/ ____\ 
                    /   \  ___|    |      ______ |  |/  ___\   __\ 
                    \    \_\  |    |___  /_____/ |  |\___ \ |  |   
                     \______  |_______ \         |__/____  >|__|   
                            \/        \/                 \/        
                            """
print(f"{Fore.CYAN}{app_ascii}{Style.RESET_ALL}")

ticbig = time.time()

filereader = open("testlist.glf", "r")
num_games = 0
for line in filereader:
    num_games += 1
filereader.close()

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

def tester():
    num_processing = 0
    last_tt = 0
    time_sum = 0

    game_title = "Doom 8"
    game_price = 59.99
    num_games = 29
    print(f"[{Fore.CYAN}GL-isf/init{Style.RESET_ALL}] Initializing {Style.BRIGHT}{app_info.name}{Style.RESET_ALL} v{Style.BRIGHT}{app_info.version}{Style.RESET_ALL} by {Style.BRIGHT}{app_info.by}{Style.RESET_ALL}\n")
    for counter in range(num_games):
        num_processing += 1
        tic = time.time()

        time_sum += last_tt
        if last_tt == 0:
            eta = "~"
            eta_avg = "~"
        else:
            eta = round((num_games - num_processing * last_tt) / 60, 2)
            # eta_avg = round(((num_games - num_processing) * (time_sum / (num_processing - 1))) / 60, 2)
            eta_avg = round((num_games - num_processing) * (time_sum / (num_processing - 1)), 2)
            eta_avg = time_convert(eta_avg)

        print(f"{progress_bar(num_processing, num_games, eta_avg)}[{Fore.CYAN}GL-isf/import{Style.RESET_ALL}] {Style.BRIGHT}Importing{Style.RESET_ALL} game info  ... ", flush=True, end="")
        print(f"[{Fore.GREEN}OK!{Style.RESET_ALL}]")
        print(f"{progress_bar(num_processing, num_games, eta_avg)}[{Fore.CYAN}GL-isf/scrape{Style.RESET_ALL}] {Style.BRIGHT}Scraping{Style.RESET_ALL} AKS.url of {Fore.BLUE}{game_title}{Style.RESET_ALL}  ... ", flush=True, end="")
        print(f"[{Fore.GREEN}OK!{Style.RESET_ALL}]")
        time.sleep(3)
        print(f"{progress_bar(num_processing, num_games, eta_avg)}[{Fore.CYAN}GL-isf/scrape{Style.RESET_ALL}] {Style.BRIGHT}Scraping{Style.RESET_ALL} AKS.lowest.price of {Fore.BLUE}{game_title}{Style.RESET_ALL}  ... ", flush=True, end="")
        print(f"[{Fore.GREEN}OK!{Style.RESET_ALL}]")
        toc = time.time()
        tictoc = round(toc - tic, 2)
        last_tt = tictoc
        print(f"{progress_bar(num_processing, num_games, eta_avg)}[{Fore.CYAN}GL-isf/proc-m{Style.RESET_ALL}] Processed {Fore.BLUE}{game_title}{Style.RESET_ALL} / {Fore.YELLOW}{game_price}e{Style.RESET_ALL} in {Style.BRIGHT}{tictoc}s{Style.RESET_ALL}")
    return()
# print(tester())
# exit()

print(f"[{Fore.CYAN}GL-isf/init{Style.RESET_ALL}] Initializing {Style.BRIGHT}{app_info.name}{Style.RESET_ALL} v{Style.BRIGHT}{app_info.version}{Style.RESET_ALL} by {Style.BRIGHT}{app_info.by}{Style.RESET_ALL}")

num_processing = 0
last_tt = 0
time_sum = 0
glf_reader = open("testlist.glf", "r")
error_counter = 0
warning_counter = 0
success_counter = 0
for line in glf_reader:
    tic = time.time()
    num_processing += 1
    time_sum += last_tt
    if last_tt == 0:
        eta = "~"
        eta_avg = "~"
    else:
        eta = round(((num_games - num_processing) * last_tt) / 60, 2)
        # eta_avg = round(((num_games - num_processing) * (time_sum / (num_processing - 1))) / 60, 2)
        eta_avg = round((num_games - num_processing) * (time_sum / (num_processing - 1)), 2)
        eta_avg = time_convert(eta_avg)
    print(f"{progress_bar(num_processing, num_games, eta_avg)}[{Fore.CYAN}GL-isf/import{Style.RESET_ALL}] {Style.BRIGHT}Importing{Style.RESET_ALL} game info  ... ", flush=True, end="")
    stripped_line = line.strip()
    game_title = ""
    steam_url = ""
    division = False
    countdown = 4
    for idx in range(len(stripped_line)):
        char = stripped_line[idx]
        try:
            if stripped_line[idx + 1] == " " and stripped_line[idx + 2] == "-" and stripped_line[idx + 4] == " ":
                division = True
        except:
            pass
        if division == True:
            countdown -= 1
        if division == True and countdown < 0:
            steam_url += char
        elif countdown >= 3:
            game_title += char
    print(f"[{Fore.GREEN}OK!{Style.RESET_ALL}]")
    # print(f"title: {game_title} url: {steam_url}")

    print(f"{progress_bar(num_processing, num_games, eta_avg)}[{Fore.CYAN}GL-isf/scrape{Style.RESET_ALL}] {Style.BRIGHT}Scraping{Style.RESET_ALL} AKS.url of {Fore.BLUE}{game_title}{Style.RESET_ALL}  ... ", flush=True, end="")
    driver = webdriver.Firefox()
    driver.get("https://www.allkeyshop.com/blog/catalogue/")
    elem = driver.find_element_by_id('search-form-keywords')
    elem.clear()
    elem.send_keys(game_title)
    # time.sleep(2)
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results-row-link")))
    first_match = driver.find_element_by_class_name('search-results-row-link')
    first_match.send_keys(Keys.RETURN)
    time.sleep(0.5)
    aks_url = driver.current_url
    assert "No results found." not in driver.page_source
    driver.close()
    if "catalogue" in aks_url:
        print(f"[{Fore.RED}FAIL!{Style.RESET_ALL}]")
        error_counter += 1
    else:
        print(f"[{Fore.GREEN}OK!{Style.RESET_ALL}]")
    # print(aks_url)

    print(f"{progress_bar(num_processing, num_games, eta_avg)}[{Fore.CYAN}GL-isf/scrape{Style.RESET_ALL}] {Style.BRIGHT}Scraping{Style.RESET_ALL} AKS.lowest.price of {Fore.BLUE}{game_title}{Style.RESET_ALL}  ... ", flush=True, end="")
    aks_proc = urllib.request.urlopen(aks_url).read()
    soup = BeautifulSoup(aks_proc, "lxml")
    pricefinder = soup.find(itemprop="lowPrice")
    ff = False
    sf = False
    game_price = ""
    for char in str(pricefinder):
        if char == '"' and ff == False:
            ff = True
        elif char == '"' and ff == True:
            sf = True
        elif ff == True and sf == False:
            game_price += char
        else:
            pass
    if not game_price and "catalogue" in aks_url:
        print(f"[{Fore.RED}FAIL!{Style.RESET_ALL}]")
        game_price_str = f"{Fore.RED}ERROR!{Style.RESET_ALL}"
    elif not game_price:
        print(f"[{Fore.YELLOW}NOT_FOUND!{Style.RESET_ALL}]")
        game_price_str = f"{Fore.YELLOW}DMC!{Style.RESET_ALL}"
        warning_counter += 1
    else:
        print(f"[{Fore.GREEN}OK!{Style.RESET_ALL}]")
        game_price_str = f"{Fore.GREEN}{game_price}e{Style.RESET_ALL}"
        success_counter += 1
    toc = time.time()
    tictoc = round(toc - tic, 2)
    tac = round(toc - ticbig, 2)
    last_tt = tictoc
    # print(game_price)
    # print(f"{progress_bar(num_processing, num_games, eta_avg)}[{Fore.CYAN}GL-isf/proc-m{Style.RESET_ALL}] Processed {Fore.BLUE}{game_title}{Style.RESET_ALL} / {game_price_str} in {Style.BRIGHT}{tictoc}s{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}-->{Style.RESET_ALL} [{Fore.CYAN}GL-isf/sgp-cmsg{Style.RESET_ALL}] Processed {Fore.BLUE}{game_title}{Style.RESET_ALL} / {game_price_str} in {Style.BRIGHT}{tictoc}s{Style.RESET_ALL}. {Style.BRIGHT}{time_convert(tac)}{Style.RESET_ALL} elapsed and {Style.BRIGHT}{eta_avg}{Style.RESET_ALL} left.")
glf_reader.close()

tocbig = time.time()
tictocbig = round(tocbig - ticbig, 2)
success_percentage = (success_counter + warning_counter) / num_games * 100
if success_percentage >= 80:
    success_percentage = f"{Fore.GREEN}{success_percentage}%{Style.RESET_ALL}"
elif success_percentage >= 60:
    success_percentage = f"{Fore.YELLOW}{success_percentage}%{Style.RESET_ALL}"
else:
    success_percentage = f"{Fore.RED}{success_percentage}%{Style.RESET_ALL}"

print(f"\n[{Fore.CYAN}GL-isf/fin{Style.RESET_ALL}] Operation {Style.BRIGHT}completed{Style.RESET_ALL} in {Style.BRIGHT}{time_convert(tictocbig)}{Style.RESET_ALL}! Success ratio is {success_percentage} - {Fore.GREEN}{success_counter}{Style.RESET_ALL} succesful, {Fore.YELLOW}{warning_counter}{Style.RESET_ALL} warnings and {Fore.RED}{error_counter}{Style.RESET_ALL} errors.  Your data is saved in {Fore.MAGENTA}save_file.ext{Style.RESET_ALL}\n")
print(f"{Fore.CYAN}{app_ascii}{Style.RESET_ALL}")
print(f"Thanks for using {Style.BRIGHT}{app_info.name}{Style.RESET_ALL} v{Style.BRIGHT}{app_info.version}{Style.RESET_ALL} by {Style.BRIGHT}{app_info.by}{Style.RESET_ALL}")

# exstr = "Supraland -- https://store.steampowered.com/app/813630/"
# g_title = ""
# s_url = ""
# division = False
# c_down = 4
# for idx in range(len(exstr)):
#     char = exstr[idx]
#     try:
#         if exstr[idx + 1] == " " and exstr[idx + 2] == "-" and exstr[idx + 4] == " ":
#             division = True
#     except:
#         pass
#     if division == True:
#         c_down -= 1
#     if division == True and c_down < 0:
#         s_url += char
#     elif c_down >= 3:
#         g_title += char

# print(f"title: {g_title} - url: {s_url}")

# glf_reader = open("testlist.glf", "r")
# for line in glf_reader:
#     stripped_line = line.strip()
#     game_title = ""
#     steam_url = ""
#     division = False
#     countdown = 4
#     for idx in range(len(stripped_line)):
#         char = stripped_line[idx]
#         try:
#             if stripped_line[idx + 1] == " " and stripped_line[idx + 2] == "-" and stripped_line[idx + 4] == " ":
#                 division = True
#         except:
#             pass
#         if division == True:
#             countdown -= 1
#         if division == True and countdown < 0:
#             steam_url += char
#         elif countdown >= 3:
#             game_title += char
#     print(f"title: {game_title} url: {steam_url}")
# glf_reader.close()