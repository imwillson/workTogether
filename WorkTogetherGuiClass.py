import tkinter as tk
import tkinter.messagebox
from CreateNewProjectGui import *
from ProjectManager import *
from SetFreeTimeGui import *
PROJECT_ID_ROW = 1
WIDTH_TWENTY_FIVE = WIDTH_TWENTY_FIVE
class WorkTogetherGui:
    '''
    Creates the main plaform for all the other interacton with the softwere
    Access point to change UserPreferences, Manage Projects,
    and View Resuls
    '''
    def __init__(self, master):
        self.master = master

        self.button1 = tk.Button(self.master, text = 'Create New Project', width = WIDTH_TWENTY_FIVE, command = self.createNewProject)
        self.button2 = tk.Button(self.master, text = 'Manage Existing Project', width = WIDTH_TWENTY_FIVE, command = self.manageProject)
        self.button3 = tk.Button(self.master, text= 'Update Schedule', width = WIDTH_TWENTY_FIVE, command= self.setFreeTime)

        self.__entry = tk.Entry(self.master, width = WIDTH_TWENTY_FIVE)
        self.__projectId = tk.Entry(self.master,width=WIDTH_TWENTY_FIVE)

        self.__newProjectLabel = tk.Label(self.master, text= 'Create new Project')
        self.__manageProjectLabel = tk.Label(self.master, text='Manage Project')
        self.__userPreferencesLabel = tk.Label(self.master, text='Set Free Time')
        self.__updateScheduleLabel = tk.Label(self.master, text='Update/Add Shedules')



        self.__manageProjectLabel.grid(row=0,column=1)
        self.__projectId.grid(row=PROJECT_ID_ROW,column=1)
        self.button2.grid(row=2,column=1)
        self.__newProjectLabel.grid(row=0,column=2)
        self.__entry.grid(row=1,column=2)
        self.button1.grid(row=2,column=2)
        self.__updateScheduleLabel.grid(row=0, column=3)
        self.button3.grid(row=2, column=3)



    def createNewProject(self):
        nums = self.__entry.get()

        if self.__isDigit(nums):
            self.newWindow = tk.Toplevel(self.master)
            self.app = CreateNewProjectGUI(self.newWindow,nums)
        else:
            tk.messagebox.showwarning("Warning","Invalid number of people")

    def manageProject(self):
        projectId = self.__projectId.get()
        if self.__isDigit(projectId):
            self.manageProjectWindow = tk.Toplevel(self.master)
            self.manager = ProjectManagerGUI(self.manageProjectWindow,projectId)
        else:
            tk.messagebox.showwarning("Warning","Invalid project id")


    def setFreeTime(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = SetFreeTimeGui(self.newWindow)
        tk.messagebox.showinfo("info", "Hi! Please add you preffered working times.\
        Please use a 24 hour system. Freetimes start from the top of the hour. Also,\
        Remember to use the day short hand.")
    def __notEmpty(self,entry):
        return entry
    def __isDigit(self,entry):
        return entry.isdigit()
