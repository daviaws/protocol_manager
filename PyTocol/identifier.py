from uuid import uuid4

__instance = None

class __Inner():

    def __init__(self, uids=[]):
        self.uids = []

    def generate_uid(self):
        return uuid4().int

    def uid_exists(self, uid):
        return uid in self.uids

    def new_uid(self):
        uid = self.generate_uid()
        while self.uid_exists(uid):
            uid = self.generate_uid()
        self.uids.append(uid)
        return uid

    def get_uids(self):
        return self.uids

def get_identifier(uids=[]):
    global __instance
    if not __instance:
        __instance = __Inner(uids)
    return __instance
