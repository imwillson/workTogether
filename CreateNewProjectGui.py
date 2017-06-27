'''
Shehtab Zaman
szaman5@binghamton.edu
CA Nuri Ra


Willson Li
wli75@binghamton.edu
CA Thomas Donohue

Final Project
'''


import tkinter as tk
import tkinter.messagebox
import NewProject
import datetime
import time

TWO_INCREMENT = 2
COLUMN_ZERO = 0
COLUMN_ONE = 1
WIDTH_TWENTY_FIVE = 25

class CreateNewProjectGUI:
    nameDict = {}
    emailDict = {}
    labelDict = {}

    def __init__(self, master, numMember):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.model = NewProject.NewProject()
        numMember = int(numMember)

        even = 0
        odd = 1
        for each in range(numMember):
            even = even + TWO_INCREMENT
            odd = odd + TWO_INCREMENT

            labelName = tk.Label(self.master, text="Member Name "+str(each + 1)+": ")
            labelName.grid(row= even,column=COLUMN_ZERO)
            tempNameEntry = tk.Entry(self.master)
            tempNameEntry.grid(row=even,column=COLUMN_ONE)

            labelEmail = tk.Label(self.master, text="Member Email "+str(each + 1)+": ")
            labelEmail.grid(row=odd ,column=COLUMN_ZERO)
            tempEmailEntry = tk.Entry(self.master)
            tempEmailEntry.grid(row=odd,column=COLUMN_ONE)

            self.nameDict["name"+str(each)] = tempNameEntry
            self.emailDict["email"+str(each)] = tempEmailEntry
        self.quitButton = tk.Button(self.master, text = 'Quit', width = WIDTH_TWENTY_FIVE, command = self.close_windows)
        self.retrieveButton = tk.Button(self.master, text = 'Send', width = WIDTH_TWENTY_FIVE, command = self.send)
        self.retrieveButton.grid(row = odd + 1, column=COLUMN_ZERO)
        self.quitButton.grid(row = odd + 1, column = 1)


    def close_windows(self):
        self.master.destroy()

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


    def send(self):
        tempDictionaryNamesEmails = {}
        listOfUserTimes = self.getUserPreferences()
        numItems = len(self.nameDict)
        for indices in range(numItems):
            tempDictionaryNamesEmails[self.nameDict["name"+str(indices)].get()]=\
            self.emailDict["email"+str(indices)].get()
        for key in tempDictionaryNamesEmails:
            #print(key,":",tempDictionaryNamesEmails[key])
            self.model.addNames(key,tempDictionaryNamesEmails[key])
        self.model.sendRequest()
        status = "Your project id is : "+self.model.returnStatus()
        tk.messagebox.showinfo("Info",status)

        #print(self.model.returnStatus())
