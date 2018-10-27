from mycroft import MycroftSkill, intent_file_handler
import os


class CloudNine(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        os.system('/opt/mycroft/skills/cloud-nine-skill.andlo/c9/scripts/install-sdk.sh')
        os.system("/opt/mycroft/skills/cloud-nine-skill.andlo/c9/server.js -p 8080 -w workspace -l 0.0.0.0 -a :")

    @intent_file_handler('nine.cloud.intent')
    def handle_nine_cloud(self, message):
        self.speak_dialog('nine.cloud')


def create_skill():
    return CloudNine()
