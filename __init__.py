from mycroft import MycroftSkill, intent_file_handler
import os
from git import Repo

class CloudNine(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        #SafePath = "/home/pi"
        SafePath = self.file_system.path
        AppPath = self._dir
        if self.settings.get('c9 installed') == None:
            self.log.info("Cloning c9.core from github. This takes some time....")
            Repo.clone_from("https://github.com/c9/core.git", SafePath + '/c9')
            self.log.info("Setting up c9.core. This will take some time to....")
            os.system(SafePath + '/c9/scripts/install-sdk.sh')
            self.log.info("Setting up workspace.")
            os.makedirs(SafePath + '/workspace')
            os.symlink('/opt/mycroft/skills', SafePath + '/workspace/Mycroft-skills')
            self.settings['c9 installed'] = "True"
            self.log.info("c9.core is installed and configured")
        self.log.info("Starting c9.core")
        os.system(SafePath + '/c9/server.js -p 8080 -w ' + SafePath + '/workspace -l 0.0.0.0 -a :')

    @intent_file_handler('nine.cloud.intent')
    def handle_nine_cloud(self, message):
        self.speak_dialog('nine.cloud')


def create_skill():
    return CloudNine()
