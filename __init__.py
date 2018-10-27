from mycroft import MycroftSkill, intent_file_handler
from subprocess import run
import os


class CloudNine(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    def initialize(self):
        os.system("/opt/mycroft/skills/cloud-nine-skill.andlo/c9/scripts/install-sdk.sh")
        command = "/opt/mycroft/skills/cloud-nine-skill.andlo/c9/server.js -p 8080 -w /home/pi/workspace -l 0.0.0.0 -a :"
        run(command.split(command)

    @intent_file_handler('nine.cloud.intent')
    def handle_nine_cloud(self, message):
        self.speak_dialog('nine.cloud')


def create_skill():
    return CloudNine()
    
def bash(command):
        run(command.split())

    
