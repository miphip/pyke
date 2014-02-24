'''
Main entry point
Created on Feb 18, 2014

@author: mikael
'''

import sys
import os

class PykeMain(object):
    
    def __init__(self):
        print "in main"
        print sys.argv
        print os.getcwd()
        pykefile = __import__('Pykefile', level=0)
        print pykefile


if sys.argv[0].endswith("__main__.py"):
    sys.argv[0] = "python -m pyke"

PykeMain()
