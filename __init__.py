from mycroft import MycroftSkill, intent_file_handler


class CloudNine(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('nine.cloud.intent')
    def handle_nine_cloud(self, message):
        self.speak_dialog('nine.cloud')


def create_skill():
    return CloudNine()
    
//
    

import 

try:
    # TODO: write code...
except Exception, e:
    raise e
else:
    # TODO: write code...
finally:
    # TODO: write code...