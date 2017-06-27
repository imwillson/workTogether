import tkinter as tk
import tkinter.messagebox
from Project import *
from PreferenceManager import *


class ProjectManagerGUI:
    DAYS = {"M":"MONDAY","T":"TUESDAY","W":"WEDNESDAY",\
    "R":"THURSDAY","F":"FRIDAY","S":"SATURDAY","N":"SUNDAY"}

    def __init__(self, master, projectId):
        self.master = master
        self.projectId = projectId
        self.model = Project(projectId)
        self.__names = []
        self.__emails = []
        self.__freeTimes = ""
        self.updateVars()

        self.__topNameLabel = tk.Label(self.master,\
        text="Members")

        self.__topEmailLabel = tk.Label(self.master,\
        text="Email")

        self.__topStatusLabel = tk.Label(self.master,\
        text="Upload Status")

        self.__topNameLabel.grid(row=0,column=1)
        self.__topEmailLabel.grid(row=0,column=2)
        self.__topStatusLabel.grid(row=0,column=3)



        rowNumber = 1
        for eachInfo in range(len(self.__names)):
            labelName = tk.Label(self.master,\
            text=self.__names[eachInfo])
            labelEmail = tk.Label(self.master,\
            text=self.__emails[eachInfo])
            #print(self.__freeTimes[eachInfo])
            if self.__isUploaded(self.__freeTimes[eachInfo]):
                labelStatus = tk.Label(self.master,\
                text="Uploaded Schedule")
            else:
                labelStatus = tk.Label(self.master,\
                text="Not Available")


            labelName.grid(row=rowNumber,column=1)
            labelEmail.grid(row=rowNumber,column=2)
            labelStatus.grid(row=rowNumber,column=3)
            rowNumber = rowNumber + 1


        #self.frame = tk.Frame(self.master)
        self.updateButton = tk.Button(self.master, text= 'Update', width = 25, command = self.updateVars)
        self.quitButton = tk.Button(self.master, text = 'Quit', width = 25, command = self.closeWindows)
        self.updateButton.grid(row=rowNumber, column=2)
        self.quitButton.grid(row=rowNumber, column=3)

        #self.frame.pack()
    def closeWindows(self):
        self.master.destroy()

    def updateVars(self):
        self.sendUsePreferences()
        self.model.updateAll()
        self.__emails=self.model.getEmails()
        self.__names=self.model.getNames()
        self.__freeTimes=self.model.getFreeTimes()
        listOfTimes = self.model.freeTimeFinder(self.showFreeTimes())
        tk.messagebox.showinfo("Info", self.__createMessage(listOfTimes))
        #print(self.showFreeTimes())
        #print(self.__freeTimes)

    def __isUploaded(self,val):
        return val != "None"

    def __createMessage(self,freeTimeList):
        message = ""
        if not freeTimeList:
            message = "Unfortunately looks like you \
            you guys don't have any free time together\
            Try updating your schedules or dare we say, \
            talk to one another. "
        else:
            message = message +  "Congrats! You have free time together at: \n"
            for eachTime in freeTimeList:
                startTime = eachTime[:-1]
                endTime = str(int(startTime)+1)
                message  = message + self.DAYS[eachTime[-1]]+" From: " + startTime +\
                " To: "+ endTime + "\n"
        return message

    def showFreeTimes(self):
        freeTimes = self.__freeTimes.split("__")
        tempTimesHolder = []
        userIndex = 0
        tempDictHolder = {}
        for each in freeTimes:
            each.strip("[]")
            each.rstrip()
            #print(each)
            tempList = each.split("\n")
            #print(tempList)

            for eachSchedule in tempList:
                if "\n" not in eachSchedule:
                         tempDictHolder['user'+str(userIndex)] = eachSchedule
                         userIndex += 1
        returnDict = {}
        for eachKey in tempDictHolder:
            if tempDictHolder[eachKey]:
                processedString = tempDictHolder[eachKey].strip("[]")
                processedString = processedString.strip("\'\'")

                removeCommas = processedString.split(", ")
                removeExtraQoutes = "".join(removeCommas).split("\"")
                temporaryList = []
                for eachTime in removeExtraQoutes:
                    if len(eachTime) > 0:
                        temporaryList.append(eachTime)
                returnDict[eachKey] = temporaryList

        return returnDict
    def getUserPreferences(self):
        try:
            userPreferences = open("userPreferences.txt","r")
            try:
                listOfTimes = []
                for eachTime in userPreferences:
                    listOfTimes.append(eachTime)
            except Exception as e:
                tk.messagebox.showwarning("Error", "Please add/update user info first")

        except Exception as e:
            tk.messagebox.showwarning("Error", "Please add/update user info first")
        return listOfTimes
    def sendUsePreferences(self):
        userPreferences = self.getUserPreferences()
        preferenceManager = PreferenceManager(userPreferences,self.projectId)
        preferenceManager.updateAll()
        #print(preferenceManager.getUpdate())
