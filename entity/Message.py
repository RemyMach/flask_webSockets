import json

class Message:

    # dict{} dict
    def __init__(self, dict=None):
        if dict is not None:
            self.fieldMessage = dict['fieldMessage']
            self.idUser = dict['idUser']
        else:
            self.fieldMessage = ""
            self.idUser = 0

    def toJson(self):
        return self.__dict__