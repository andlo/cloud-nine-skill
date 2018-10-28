# <img src='https://raw.githubusercontent.com/c9/core/master/plugins/c9.ide.theme.flat/images/cloud9_logo%402x.png'  card_color='#40DBB0' width='50' height='50' style='vertical-align:bottom'/> Cloud Nine
Installs and configure a local Cloud9 IDE

## Initial release
This skill will install and work, but still needs som love and chnges.

## About 
This skill installs and configure a local Cloud9 IDE for use to make, edit and manipulate skills on a Mycroft device.

Cloud9 is a full blown IDE accesable throug a webbrowser. That makes it ideal to make and devolep skills to and on a Mycroft device
It also includes a fulls shell so using git to push and pull is easyly done. Offcause alsp specifik Mycroft stuff like mycroft-msk can be run directly from here.

This is a local installation on your devices. So no data or anything to do whith Amazon AWS, Cloud9 and related online services. 


Notise it takes a little time to install. After install you can access cloud9 ide at http://<hostname_of_device>:8080

## Credits 
Andreas Lorensen (@andlo)

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