from mycroft import MycroftSkill, intent_file_handler


class Prova(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('prova.intent')
    def handle_prova(self, message):
        self.speak_dialog('prova')


def create_skill():
    return Prova()

