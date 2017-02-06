from base_types import Nameable, Identifiable

class Event(Nameable, Identifiable):
        
    def __init__(self, uid, name='', params={}):
        Identifiable.__init__(self, uid)
        Nameable.__init__(self, name)
        self.params = params

    # def list_elements(self):
    #     elements = ''
    #     for key, value in sorted(self.params.items()):
    #         if not elements:
    #             elements = 'Params:\n'
    #         elements += str(key) + ' : ' + str(value) + '\n'
    #     return elements

    # def prefix(self):
    #     return 'Evt:'

    # def sufix(self):
    #     return '------------------------'

    # def __repr__(self):
    #     return self.prefix() + ' ' + Nameable.__repr__(self) + '\n' + self.list_elements() + self.sufix()


class Requisition(Event):
    
    def __init__(self, uid, name='', params={}, excpected_events=[]):
        Event.__init__(self, uid, name, params)
        self.expected_events = []

    def add_evt(self, evt):
        self.expected_events.append(evt)

    def del_evt(self, evt):
        self.expected_events.remove(evt)

    # def prefix(self):
    #     return 'Req:'

    # def list_elements(self):
    #     elements = ''
    #     elements = Event.list_elements(self)
    #     elements += 'Events:\n'
    #     for evt in self.expected_events:
    #         elements += evt.get_name() + '\n'
    #     return elements
