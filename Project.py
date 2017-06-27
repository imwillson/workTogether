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


INDEX_ZERO = 0
INDEX_ONE = 1
INDEX_TWO = 2

IP_ADDRESS_STATUS = "http://127.0.0.1:5000/ProjectStatus"
IP_ADDRESS_FREETIME = "http://127.0.0.1:5000/FreeTime"
class Project():
    """docstring for Project"""
    def __init__(self, pid):
        #super(Project, self).__init__()
        self.__id = pid
        self.__names = []
        self.__emails = []
        self.__freeTimes = []

    def updateAll(self):
        projectData = {}
        projectData['projectId'] = self.__id
        communication = requests.get(IP_ADDRESS_STATUS, data = projectData)
        tempServerResponse = communication.text

        #print(tempServerResponse)
        memberInfo = tempServerResponse.split("\n")
        for eachMember in memberInfo:
             if eachMember:
                 tempMemberInfo = eachMember.split("-")
                 #print(eachMember)
                 #print(len(tempMemberInfo))
                 memberName = tempMemberInfo[INDEX_ZERO].strip("('\" \"')")
        #         #print(memberName)
                 memberEmail = tempMemberInfo[INDEX_ONE].strip("('\" \"')")
                 memberFreeTime = tempMemberInfo[INDEX_TWO]

                 #print(memberFreeTime)
                 if memberName:
                     self.__names.append(memberName)
                 if memberEmail:
                     self.__emails.append(memberEmail)
                 if memberFreeTime:
                      self.__freeTimes.append(memberFreeTime)
        #
        # #for names in self.__names:
        # #print(len(self.__names))
        # #print(len(self.__emails))
        # #print(len(self.__freeTimes))
        #print(self.__freeTimes)
    def getEmails(self):
        return self.__emails
    def getNames(self):
        return self.__names
    def getFreeTimes(self):
        queryData = {}
        queryData['ProjectId'] = self.__id
        com = requests.post(IP_ADDRESS_FREETIME,data=queryData)
        #print(com.text)
        return com.text

    def freeTimeFinder(self,freeTimeDict):
        theDict = {}
        try:
            for name in freeTimeDict:
                listOfTimes = freeTimeDict[name]
                for eachMember in listOfTimes:
                    tempSplit = eachMember.split("-")
        			#print(tempSplit)+
                    for interval in range(int(tempSplit[0]),int(tempSplit[INDEX_ONE])):
                        if str(interval)+tempSplit[INDEX_TWO] in theDict:
                            theDict[str(interval)+tempSplit[INDEX_TWO]] = \
                            theDict[str(interval)+tempSplit[INDEX_TWO]] + "-" + name
                        else:
                            theDict[str(interval)+tempSplit[INDEX_TWO]] = name
        except Exception as err:
            theDict = {}
    	#print(theDict)
        maximum = 0
        greatestKey = []
        greatestValue = []
        for key in theDict:
            value = theDict[key]
            numOfPeople = value.split("-")
            if len(numOfPeople) > maximum:
                maximum = len(numOfPeople)
                greatestKey = []
                greatestValue = []
                greatestKey.append(key)
                greatestValue.append(value)
            elif len(numOfPeople) == maximum:
                greatestKey.append(key)
                greatestValue.append(value)
                return greatestKey

    def __isUploaded(self,val):
        return val != "None"
