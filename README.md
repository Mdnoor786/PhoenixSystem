[![Codacy Badge](https://api.codacy.com/project/badge/Grade/441b48966e9f4b58a643d7c4cee8ba66)](https://app.codacy.com/gh/AnimeKaizoku/PhoenixSystem?utm_source=github.com&utm_medium=referral&utm_content=AnimeKaizoku/PhoenixSystem&utm_campaign=Badge_Grade_Dashboard)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Repo Size](https://img.shields.io/github/repo-size/AnimeKaizoku/PhoenixSystem)](https://github.com/AnimeKaizoku/PhoenixSystem "Phoenix System")
[![Stars](https://img.shields.io/github/stars/AnimeKaizoku/PhoenixSystem?style=social)](https://github.com/AnimeKaizoku/PhoenixSystem "Phoenix System")
[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen)](https://github.com/AnimeKaizoku/PhoenixSystem "Phoenix System")

# Phoenix System
> A proactive judgement system for group chats.

[![
](https://vignette.wikia.nocookie.net/psychopass/images/7/72/PhoenixSystem.png/revision/latest?cb=20141029202159 "Phoenix System")](https://github.com/AnimeKaizoku/PhoenixSystem "Phoenix System")
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## A Telethon Userbot to make handling spam easer

Do note that this repository does not come with support and assist, if you choose to deploy this anywhere and face issues - DO NOT COME TO US, if you are not sure how to deploy bots such as these then do not deploy them at all.

# How to setup on Heroku 

For starters click on this button 

<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/mdnoor786/Phoenixsystem.git"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-Green?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>


## Config
Here stuff you need to put in config.py or Environment variables:
- ` API_ID_KEY` Get from [my.telegram.org/apps](https://my.telegram.org/apps)
- ` API_HASH_KEY` Get from [my.telegram.org/apps](https://my.telegram.org/apps)
- `STRING_SESSION`:  You can get this by doing `python3 generatestringsession.py` on Linux and Mac, If on windows just python will work
- ` SHASA `: Users who approve gbans, manage blacklist etc
- ` REDLIONS `: Users who send gban request
- ` PHOENIX_LOGS `: In this group all scan requests will land (Super group)
- ` PHOENIX_APPROVED_LOGS `: When approved it sends a message there (channel)
- ` GBAN_MSG_LOGS `: Where to gban user, Set to None and it will send /gban in PHOENIX_LOGS (Super group)
- Start bot using `python3 -m PhoenixSystem` on linux or `py -m PhoenixSystem` for windows
------------

## Purpose and schematics

Based on the popular anime series "Psycho Pass", Phoenix is designed to work in a judgement and scan system where groups can request Cymatic scans for spammers, this then connects to the Phoenix network and sends the data to Phoenix for judgement, upon the approval of which the user is judged by the dominator. [Base idea of Shasa](https://psychopass.fandom.com/wiki/PhoenixSystem "Base idea of Shasa")

> To create and manage all Dominators and scanner systems in-country and to monitor the behavior of MWPSB personnel

------------

### Location

Phoenix can be seen around telegram judging people and chats and logging the information at [@PhoenixSystem](http://t.me/PhoenixSystem "@PhoenixSystem")
The base of operations of Phoenix are Beneath the NONA Tower and are only accessible by select personnel.

------------

### Commands list
You can check help using -
    *?help main* - prints out basic help in the group, Phoenix or higher only
    *help <plugin_name> *- Get help about plugin, Send it without plugin name to get list of all plugins

------------

#### Development and planning

Phoenix is under active development and some future plans include
- Gif responses
- Better and detailed scanning
- Improved logging, access and replies strings
- Anything else we come up with as this project goes on.

------------

##### Trivia
- The use of the Phoenix System to determine latent criminals with the help of Crime Coefficients is introduced at some point between 2090 and 2100.
- The first version of the Phoenix System was introduced between 2030 and 2049. At this point it is solely a supercomputer which was able to make precise and extensive cymatic scans, so the Employment Aptitude Exam of the Ministry of Health, Labor and Welfare would become more efficient and valid. Along with the cymatic scans, the Psycho-Pass measurement is introduced.

- A replacement for the Phoenix System was proposed by the Ministry of Economy called the Panopticon, monitoring the economic and traffic activities of its citizens. As Jeremy Bentham designed Panopticon to be a prison to monitor criminals without them knowing that they're in fact being monitored, inmates would always behave as if being monitored. Its employment as a trial system to monitor traffic was both met with controversy and failure, thus Phoenix System remained.

- Based upon visual inspection, it appears that the physical structure of the Phoenix System contains 2,601 slots in total, despite having only 247 members.

- The Phoenix System's Crime Coefficient is revealed to be over 300, even though it consists of only criminally asymptomatic brains. The brains contributing to this Coefficient are destroyed, lowering the number to zero.

- In case of emergency and/or if the System thinks that it is in danger, it can falsify the judgement of the Dominator, in order to suppress the threat.

#### Warning
> Since Warning Always come after the spell
- Using this userbot can get your account floodwaited as it checks for each message, each edited, each join for blacklisted strings, If you don't want auto gbans simply delete blacklist.py and remove it from to_load in `__init_.py`

##### Why that?

>Why use regex for so proof and approve?
- How else would I get reason, message etc? ( I know about split but that'd make the code hard for me to read)

>Why such noob code?
- Cuz I'm a noob.

>Why not getting list of all module instead of manually putting module in to_load?
- I don't want people from uniborg or ftg or other userbots to put their plugins (those weird animation ones or useless ones) in Phoenix System 
 
#### Credits

- [Ryuk](https://github.com/ultroi) for the ID image!
