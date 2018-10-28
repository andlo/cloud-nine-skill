from mycroft import MycroftSkill, intent_file_handler
import os



class CloudNine(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        # SafePath = self.filesystem.path()
        AppPath = self._dir
        if self.settings.get('c9 installed') == None:
            os.system('git clone https://github.com/c9/core.git ' + AppPath + '/c9')
            os.system(AppPath + '/c9/scripts/install-sdk.sh')
            self.settings['c9 installed'] = 'True'
        try:
            os.system(AppPath + '/c9/server.js -p 8080 -w ' + AppPath + '/workspace -l 0.0.0.0 -a :')
        
    @intent_file_handler('nine.cloud.intent')
    def handle_nine_cloud(self, message):
        self.speak_dialog('nine.cloud')


def create_skill():
    return CloudNine()
