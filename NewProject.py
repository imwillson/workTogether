'''
Shehtab Zaman
szaman5@binghamton.edu
CA Nuri Ra


Willson Li
wli75@binghamton.edu
CA Thomas Donohue

Final Project
'''

import requests
import json
import time

IP_ADDRESS = "http://127.0.0.1:5000/NewProject"

class NewProject:
    def __init__(self):
        self.__requestStatus = ""
        self.__nameEmailDict = {}
    def addNames(self,strName, strEmail):
        self.__nameEmailDict[strName] = strEmail

    def sendRequest(self):
        if self.__nameEmailDict:
            userData = {}
            today = time.strftime("%Y-%m-%d")

            userData['data'] = json.dumps(self.__nameEmailDict)
            userData['date'] = today
            com = requests.post(IP_ADDRESS, data = userData)
            self.__requestStatus = com.text
    def returnStatus(self):
        return self.__requestStatus
