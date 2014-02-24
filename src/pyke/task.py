import sys


class Task(object):
    
    def __init__(self, name):
        self.name = name
        self.actions = []
        self.prerequisites = []

    def add_prerequisite(self, prereq):
        self.prerequisites.append(prereq)
    
    def add_action(self, action):
        self.actions.append(action)
    
    def invoke(self):
        if self.up_to_date():
            return
        for prereq in self.prerequisites:
            prereq.invoke()
        for action in self.actions:
            action()

    def up_to_date(self):
        return False

    def time_stamp(self):
        return sys.float_info.min