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
from Project import *

ROW_ONE = 1
ROW_TWO =  2
ROW_THREE = 3
ROW_FOUR = 4
ROW_FIVE = 5
ROW_SIX = 6
ROW_SEVEN  = 7
ROW_EIGHT = 8
ROW_NINE = 9
COLUMN_ZERO = 0
COLUMN_ONE = 1
COLUMN_TWO = 2
COLUMN_THREE = 3
COLUMN_FOUR = 4
COLUMN_FIVE = 5
HOURS_IN_DAY = 24
DAYS = ["M","T","W","R","F","S","N"]
class SetFreeTimeGui:
    def __init__(self, master):
        self.master = master
        self.quitButton = tk.Button(self.master, text = 'Quit', width = 25, command = self.closeWindows)
        self.quitButton.grid(row=ROW_EIGHT, column=COLUMN_THREE)

        self.updateButton = tk.Button(self.master, text = 'Update', width = 25, command = self.updateTimes)
        self.updateButton.grid(row=ROW_EIGHT, column=COLUMN_TWO)

        self.labelFromOne = tk.Label(self.master,text="From")
        self.labelFromTwo = tk.Label(self.master,text="From")
        self.labelFromThree = tk.Label(self.master,text="From")

        self.entryOneFrom = tk.Entry(self.master)
        self.entryTwoFrom = tk.Entry(self.master)
        self.entryThreeFrom = tk.Entry(self.master)

        self.labelToOne = tk.Label(self.master,text="To")
        self.labelToTwo = tk.Label(self.master,text="To")
        self.labelToThree = tk.Label(self.master,text="To")

        self.entryOneTo = tk.Entry(self.master)
        self.entryTwoTo = tk.Entry(self.master)
        self.entryThreeTo = tk.Entry(self.master)

        self.labelDayOne = tk.Label(self.master,text="Day")
        self.labelDayTwo = tk.Label(self.master,text="Day")
        self.labelDayThree = tk.Label(self.master,text="Day")

        self.entryOneDay = tk.Entry(self.master)
        self.entryTwoDay = tk.Entry(self.master)
        self.entryThreeDay = tk.Entry(self.master)

        self.nameLabel = tk.Label(self.master,text="Name: ")
        self.emailLabel = tk.Label(self.master,text="Email: ")


        self.labelFromOne.grid(row=ROW_TWO,column=COLUMN_ZERO)
        self.labelFromTwo.grid(row=ROW_FOUR,column=COLUMN_ZERO)
        self.labelFromThree.grid(row=ROW_SIX,column=COLUMN_ZERO)

        self.labelToOne.grid(row=ROW_TWO,column=COLUMN_TWO)
        self.labelToTwo.grid(row=ROW_FOUR,column=COLUMN_TWO)
        self.labelToThree.grid(row=ROW_SIX,column=COLUMN_TWO)

        self.labelDayOne.grid(row=ROW_TWO,column=COLUMN_FOUR)
        self.labelDayTwo.grid(row=ROW_FOUR,column=COLUMN_FOUR)
        self.labelDayThree.grid(row=ROW_SIX,column=COLUMN_FOUR)


        self.entryOneFrom.grid(row=ROW_TWO,column=COLUMN_ONE)
        self.entryTwoFrom.grid(row=ROW_FOUR,column=COLUMN_ONE)
        self.entryThreeFrom.grid(row=ROW_SIX,column=COLUMN_ONE)

        self.entryOneTo.grid(row=ROW_TWO,column=COLUMN_THREE)
        self.entryTwoTo.grid(row=ROW_FOUR,column=COLUMN_THREE)
        self.entryThreeTo.grid(row=ROW_SIX,column=COLUMN_THREE)

        self.entryOneDay.grid(row=ROW_TWO,column=COLUMN_FIVE)
        self.entryTwoDay.grid(row=ROW_FOUR,column=COLUMN_FIVE)
        self.entryThreeDay.grid(row=ROW_SIX,column=COLUMN_FIVE)

        self.entryName=tk.Entry(self.master)
        self.entryEmail = tk.Entry(self.master)

        self.nameLabel.grid(row=ROW_SEVEN,column=COLUMN_ZERO)
        self.entryName.grid(row=ROW_SEVEN,column=COLUMN_ONE)
        self.emailLabel.grid(row=ROW_SEVEN,column=COLUMN_TWO)
        self.entryEmail.grid(row=ROW_SEVEN,column=COLUMN_THREE)

        self.helperLabel = tk.Label(self.master,text="Monday is M, Thursday is R and Sunday is N. \
        \nWe trust you get the rest (HINT: First Letter)")
        self.helperLabel.grid(row = 9)
        ##self.firstDayPref = tk.StringVar()
        ##self.selectionOne = tk.Combobox(self.master, textvariable=self.firstDayPref)

    def closeWindows(self):
        self.master.destroy()

    def checkInputs(self, val1, val2):
        try:
            returnValue = (int(val2) - int(val1))>0
            if returnValue:
                returnValue = int(val2) < HOURS_IN_DAY + 1

                if returnValue:
                    returnValue = int(val1) < HOURS_IN_DAY + 1
        except Exception:
            returnValue = False
        return returnValue

    def updateTimes(self):
        securityCheck = True
        if not self.checkInputs(self.entryOneFrom.get(), self.entryOneTo.get()):
            tk.messagebox.showwarning("Error","Invalid Input in First Preference")
            securityCheck = False
        if not self.checkInputs(self.entryTwoFrom.get(), self.entryTwoTo.get()):
            tk.messagebox.showwarning("Error","Invalid Input in Second Preference")
            securityCheck = False
        if not self.checkInputs(self.entryThreeFrom.get(), self.entryThreeTo.get()):
            tk.messagebox.showwarning("Error","Invalid Input in Third Preference")
            securityCheck = False
        if not self.entryOneDay.get() in DAYS:
            tk.messagebox.showwarning("Error","Invalid Input(Day) in First Preference")
            securityCheck = False
        if not self.entryOneDay.get() in DAYS:
            tk.messagebox.showwarning("Error","Invalid Input(Day) in Second Preference")
            securityCheck = False
        if not self.entryOneDay.get() in DAYS:
            tk.messagebox.showwarning("Error","Invalid Input(Day) in Third Preference")
            securityCheck = False





        infoOne = self.entryOneFrom.get() + "-" + \
        self.entryOneTo.get() + "-" +self.entryOneDay.get()

        infoTwo = self.entryTwoFrom.get() + "-" + \
        self.entryTwoTo.get() + "-" +self.entryTwoDay.get()

        infoThree = self.entryThreeFrom.get() + "-" + \
        self.entryThreeTo.get() + "-" +self.entryThreeDay.get()

        name = self.entryName.get()
        email = self.entryEmail.get()


        if securityCheck:
            userPreferences = open("userPreferences.txt", "w")
            userPreferences.write(name + "\n")
            userPreferences.write(email + "\n")
            userPreferences.write(infoOne + "\n")
            userPreferences.write(infoTwo + "\n")
            userPreferences.write(infoThree + "\n")
            userPreferences.close()
            self.master.destroy()

        #print(infoOne)

    #    self.model.updateAll()
