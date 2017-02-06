class Nameable():

    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __repr__(self):
        return self.name

class Identifiable():

    def __init__(self, uid):
        self.uid = uid

    def get_uid(self):
        return self.uid