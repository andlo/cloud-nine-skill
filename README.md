# <img src='https://raw.githubusercontent.com/c9/core/master/plugins/c9.ide.theme.flat/images/cloud9_logo%402x.png'  card_color='#40DBB0' width='50' height='50' style='vertical-align:bottom'/> Cloud Nine
Installs and configure a local Cloud9 IDE

## Initial release
This skill will install and work, but still needs som love and chnges.

## About 
This skill installs and configure a local Cloud9 IDE for use to make, edit and manipulate skills on a Mycroft device.

Cloud9 is a full blown IDE accesable throug a webbrowser. That makes it ideal to make and devolep skills to and on a Mycroft device
It also includes a fulls shell so using git to push and pull is easyly done. Offcause alsp specifik Mycroft stuff like mycroft-msk can be run directly from here.

This is a local installation on your devices. So no data or anything to do whith Amazon AWS, Cloud9 and related online services. 

#### How to install Cloud Nine Skill
Install Cloud Nine skill by …
```
msm install https://github.com/andlo/cloud-nine-skill.git
``` 
Install will install some exras on your device. That is nodejs, tmux and sqlite.
Initialazion will take quite some time and includes
* git download of c9.core
* compiling c9 node modules and extras
* setting up workspace

Duing install there is a lot of output in the log. It should however endup with the line “Cloud9 is up and running”

##### How to remove Cloud Nine Skill
Remove Cloud Nine Skill by …
```
msm remove cloud-nine
```
After that delete /home/pi/.mycroft/skills/CloudNine and subfolders. Also delete /home/pi/,c9 and /home/pi/node-gyp
and if not needed by other skills
```
apt-get remove nodejs tmux sqlite3 node-sqlite3
```


## Credits 
Andreas Lorensen (@andlo)

And the nice people at Mycroft and the good comunity around Mycroft. Both is helpfull and inspirating.


## Supported Devices 
platform_mark1 platform_mark2 platform_picroft 

## Category
**Configuration**
Productivity

## Tags
#Cloud9
#C9
#IDE
#Dev

## ToDo
* Make better error handling
* Make start/stop/restart handling
* Setup specifik Mycroft runner to launch mycroft-cli-client inside shell
* Setup specifik runner to show mycroft logs
* Adding posibility to userdefined workspases throu home.mycroft.ai setttings
* Maybe Mycroft branding - speciel theme or whatever ? 