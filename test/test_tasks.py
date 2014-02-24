'''
Created on Feb 20, 2014

@author: mikael
'''
import unittest

from pyke.task import Task

unittest.TestLoader.testMethodPrefix = 'should'

class TaskTests(unittest.TestCase):


    def setUp(self):
        self.action_calls = []

    def gen_action(self, i):
        def action():
            self.action_calls.append(i)
        return action


    def should_invoke_all_actions_in_order(self):
        t = Task('myTask')
        t.add_action(self.gen_action(1))
        t.add_action(self.gen_action(2))

        t.invoke()
        self.assertSequenceEqual([1, 2], self.action_calls)


    def should_invoke_prerequisites_before_actions(self):
        t1 = Task('1')
        t1.add_action(self.gen_action(1))
        t2 = Task('2')
        t2.add_action(self.gen_action(2))
        t2.add_prerequisite(t1)

        t2.invoke()
        self.assertSequenceEqual([1, 2], self.action_calls)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_executes_']
    unittest.main()