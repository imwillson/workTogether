import requests
import json

IP_ADDRESS = "http://127.0.0.1:5000/UpdateProject"
class PreferenceManager:
    """docstring for Project"""
    def __init__(self, preferences,projectId):
        self.__name = preferences[0]
        self.__email = preferences[1]
        self.__id = projectId
        self.__freeTimes = []
        #print(len(preferences))
        for times in range(2,len(preferences)):
            tempString = preferences[times].strip("\n")
            self.__freeTimes.append(tempString)
        self.__serveResponse = ""

    def updateAll(self):
        projectData = {}
        projectData['name'] = self.__name
        projectData['email'] = self.__email
        projectData['projectId'] = self.__id
        projectData['freeTime'] = json.dumps(self.__freeTimes)
        communication = requests.post(IP_ADDRESS, data = projectData)
        tempServerResponse = communication.text
        self.__serveResponse = tempServerResponse
    def getUpdate(self):
        return self.__serveResponse
