## [GL-isf] Gamelist-import.scrape.format v0.10a by darkk!

                        ________.____              .__         _____                    
                       /  _____/|    |             |__| ______/ ____\                   
     ______   ______  /   \  ___|    |      ______ |  |/  ___\   __\    ______   ______ 
    /_____/  /_____/  \    \_\  |    |___  /_____/ |  |\___ \ |  |     /_____/  /_____/ 
                       \______  |_______ \         |__/____  >|__|                      
                              \/        \/                 \/                           

**GL-isf** [*Gamelist-import.scrape.format*] Is an project to ease getting cheapest game prices available for list of games and formatting the output!

* This started as a personal project but it is morphing to something of an app
* Lots of options on formatting, types of input and output are still limited but more will be added over time!

**[ Help ]**
*[ Parameters ]*

usage: GL-isf [-h] [-v] [-f [FORMAT]] input_file [output_file]

positional arguments:
  input_file            filename of gamelist to read
  output_file           filename of formatted list to write (default: [.\gamelist.glf])

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -f [FORMAT], --format [FORMAT]
                        formatting of output_file [reddit] (default: [reddit])

*[ Formatting ]*

*input_file*
1. text-store (default barter.vg export): game_name -- steam_url [Doom 8 - https://store.steampowered.com/app/xxxxxx/]

*output_file*
1. reddit: - game_title_with_steam_url - game_price(italics)  

*[ Misc ]*

- If price check has failed or price not found, then you should find games with price as "MCN!" in output_file and do manual check on those or re-run those items. (ability to do automatic re-check of failed items coming in future!)