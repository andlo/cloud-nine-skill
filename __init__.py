from mycroft import MycroftSkill, intent_file_handler
import os
from git import Repo

class CloudNine(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        #SafePath = "/home/pi"
        SafePath = self.file_system
        AppPath = self._dir
        if self.settings.get('c9 installed') == None:
            Repo.clone_from("https://github.com/c9/core.git", AppPath + '/c9')
            os.system(AppPath + '/c9/scripts/install-sdk.sh')
            os.makedirs(SafePath + '/workspace')
            os.symlink('/opt/mycroft/skills', SafePath + '/workspace/Mycroft-skills')
            self.settings['c9 installed'] = 'True'
        os.system(AppPath + '/c9/server.js -p 8080 -w ' + SafePath + '/workspace -l 0.0.0.0 -a :')

    @intent_file_handler('nine.cloud.intent')
    def handle_nine_cloud(self, message):
        self.speak_dialog('nine.cloud')


def create_skill():
    return CloudNine()
