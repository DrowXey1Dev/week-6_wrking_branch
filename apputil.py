#-----EXERCISE 1-----#
#-----IMPORTS-----#
import os
import pandas as pd
import genius_api
import requests

#class for Genius instantiation
class Genius:
    def __init__(self, access_token = None):
        #take passed token to use, or fall back to environment variable if none is provided
        self.access_token = access_token or os.environ.get("ACCESS_TOKEN")

#test code (call from external main)
'''
from apputil import Genius
genius = Genius()
print(genius.access_token)
'''
