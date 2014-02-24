import os
from pyke.task import Task


class FileSystem(object):
            
    def exists(self, path):
        return os.path.exists(path)
        
    def mtime(self, path):
        return os.path.getmtime(path)


class FileTask(Task):
    fs = FileSystem()
    
    def __init__(self, target_path):
        Task.__init__(self, target_path)

    def up_to_date(self):
        if not self.fs.exists(self.name):
            return False
        return all(self.time_stamp() >= prereq.time_stamp() for prereq in self.prerequisites)

    def time_stamp(self):
        if not self.fs.exists(self.name):
            return Task.time_stamp(self)
        return self.fs.mtime(self.name)
