from base_types import Nameable, Identifiable
from copy import deepcopy

class Protocol(Nameable, Identifiable):

    def __init__(self, uid, name='', rules={}):
        Identifiable.__init__(self, uid)
        Nameable.__init__(self, name)
        self.rules = rules     

    def add_rule(self, rule):
        rule_id = rule.get_uid()
        self.rules[rule_id] = rule

    def del_rule(self, rule):
        rule_id = rule.get_uid()
        del self.rules[rule_id]

    def copy_rule(self, uid):
        rule = self.get_rule(uid)
        self.add_rule(rule)

    def get_rule(self, uid):
        return deepcopy(self.rules[uid])

    def get_rules(self):
        return deepcopy(self.rules)
