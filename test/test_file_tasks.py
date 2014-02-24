'''
Created on Feb 20, 2014

@author: mikael
'''
import unittest

from pyke.file_task import FileTask, FileSystem
import os

unittest.TestLoader.testMethodPrefix = 'should'


class FileTaskTest(unittest.TestCase):

    class FakeFileSystem(FileSystem):
        def __init__(self, files_dict):
            self.files = files_dict
            
        def exists(self, path):
            return self.files.has_key(path)
            
        def mtime(self, path):
            if path not in self.files:
                raise os.error()
            return self.files[path]
        

    def setUp(self):
        self.action_calls = []
        self.file_system = FileTaskTest.FakeFileSystem({ 'f1': 1, 'f2': 2, 'f3': 3 })
        FileTask.fs = self.file_system
        self.ft1 = FileTask('f1')
        self.ft1.add_action(self.gen_action(1))
        self.ft2 = FileTask('f2')
        self.ft2.add_action(self.gen_action(2))
        self.ft3 = FileTask('f3')
        self.ft3.add_action(self.gen_action(3))


    def gen_action(self, i):
        def action():
            self.action_calls.append(i)
        return action
        
        
    def should_invoke_actions_if_non_existent(self):
        t = FileTask('non_existant_file_path')
        t.add_action(self.gen_action(1))

        t.invoke()
        self.assertSequenceEqual([1], self.action_calls)
        
        
    def should_not_invoke_actions_if_file_exists_and_has_no_prerequisites(self):
        self.ft1.invoke()
        self.assertSequenceEqual([], self.action_calls)
        
        
    def should_invoke_actions_if_older_than_any_prerequisite(self):
        self.ft2.add_prerequisite(self.ft1)
        self.ft2.add_prerequisite(self.ft3)

        self.ft2.invoke()
        self.assertSequenceEqual([2], self.action_calls)
        
        
    def should_not_invoke_actions_if_newer_than_all_prerequisites(self):
        self.ft3.add_prerequisite(self.ft1)
        self.ft3.add_prerequisite(self.ft2)

        self.ft3.invoke()
        self.assertSequenceEqual([], self.action_calls)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_executes_']
    unittest.main()