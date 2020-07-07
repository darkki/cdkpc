## [GL-isf] Gamelist-import.scrape.format v0.22a by darkk!

                        ________.____              .__         _____                    
                       /  _____/|    |             |__| ______/ ____\                   
     ______   ______  /   \  ___|    |      ______ |  |/  ___\   __\    ______   ______ 
    /_____/  /_____/  \    \_\  |    |___  /_____/ |  |\___ \ |  |     /_____/  /_____/ 
                       \______  |_______ \         |__/____  >|__|                      
                              \/        \/                 \/                           

**GL-isf** [*Gamelist-import.scrape.format*] Is an project to ease getting cheapest game prices available for list of games and formatting the output!

* This started as a personal project but it is morphing to something of an app
* Lots of options on formatting, types of input and output are still limited but more will be added over time!

**[ Help - Parameters ]**

usage: GL-isf [-h] [-v] [-f [FORMAT]] input_file [output_file] 

positional arguments:\
  input_file            filename of gamelist to read\
  output_file           filename of formatted list to write (default: [.\gamelist.glf]) 

optional arguments:\
  -h, --help            show this help message and exit\
  -v, --version         show program's version number and exit\
  -f [FORMAT], --format [FORMAT]\
                        formatting of output_file [reddit] (default: [reddit])\
  -if [INPUT_FORMAT], --input_format [INPUT_FORMAT] 
                        formatting of input_file [text-store] (default: [text-store]) 
  -ar, --autorecheck    enables automatic re-checking of failed scrapes 

**[ Help - Formatting ]**

*input_file*
1. text-store (default barter.vg export): game_name -- steam_url [Doom 8 - https://store.steampowered.com/app/xxxxxx/]

*output_file*
1. reddit: (unordered_list) game_title(linked_to_steam_url) - game_price(bold&italics)  

**[ Help - Misc ]**

- If price check (and auto-recheck)has failed or price not found, then after processing you should find games with price as "MCN!" in output_file and do manual check on those or re-run those items.
- If autorecheck is enabled, GL-isf will automatically try to re-scrape failed item once with more reliability (slightly slower too).
- More input/output_file formats will be coming in future. Plus input_file format auto-detection and maybe configurable output formatting.