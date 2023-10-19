"""
__main__.py
The main program file for the alphabetical sorter
10/19
"""

import customtkinter
from tkinter import messagebox
import string
import os
import settings
import statistics

class App(customtkinter.CTk):
    
    def __init__(self) -> None:
        super().__init__()
        
        #consts
        self.Alphabet = tuple(string.ascii_letters)
        #Vars
        
        self.rawLength:int = 0
        
        #list to store data being modified
        self.textData:list = []
        
            #Dim Vars
        self.h, self.w = str(int(self.winfo_screenheight()/2)), str(int(self.winfo_screenwidth()/2)) # set variaible h(height) w(width) to 1/2 the native screen size
        self.defaultDimensions = self.w + "x" + self.h #make a string compatible with the tkinter geometry() function
        self.resizable(width=False, height=False)
        #Startup/Interfacing Functions
        
            #title at the top of the box
        self.title("Alphabetical Sorter")
        
            #apply previous dimensions
        self.resetDims()
        
            #appFrame for a center container 
        self.appFrame = customtkinter.CTkFrame(master=self, width=int(self.w)/1.5, height=int(self.h)/1.25)
        self.appFrame.place(x=200, y=50)
        
        #LABELS
        
        self.mainlabel = customtkinter.CTkLabel(master=self, width=8,height=5,text=f"TextConverter & Sorter \nversion{version}\n artyom curtis")
        self.mainlabel.place(x = 20, y = 25)
        
        #the entry widget in the middle of screen to display the data you are manipulating
        self.labelReturn = customtkinter.CTkEntry(master=self.appFrame, width=300, height= 90)
        self.labelReturn.place(x=75, y= 25)
        
        self.dataOptionboxlabel = customtkinter.CTkLabel(master = self, text= "File Selection")
        self.dataOptionboxlabel.place(x=35, y=75)
        
        self.typeLabel = customtkinter.CTkLabel(master=self, text="Output Type")
        self.typeLabel.place(x=25,y=235)
        
        #LABELS
        
        #MISC
        
        #options for input
        self.dataOptionsboxVAR = customtkinter.StringVar(value='Select Input File')
        self.dataOptionsbox = customtkinter.CTkOptionMenu(master = self, values=os.listdir(), variable=self.dataOptionsboxVAR, command=self.readFile)
        self.dataOptionsbox.place(x = 20, y = 110)

        #options for output
        self.writeOptionsboxVAR = customtkinter.StringVar(value='Select Output File')
        self.writeOptionsbox = customtkinter.CTkOptionMenu(master = self, values=os.listdir(), variable=self.writeOptionsboxVAR, command = self.writeFile)
        self.writeOptionsbox.place(x = 20, y = 145)
        
        #checkbox for binary output
        self.outputTypeBINARY = customtkinter.CTkCheckBox(master=self, text='BINARY', onvalue=1, offvalue=0)
        self.outputTypeBINARY.place(x = 20, y = 265)
        
        #MISC
        
        #BUTTONS 
        
        self.quitButton = customtkinter.CTkButton(master=self, text="Close App", command=self.quit)
        self.quitButton.place(x=20, y=200)
        
        #clear data
        self.clearInput = customtkinter.CTkButton(master=self.appFrame, text="Clear Data", command=self.clearData)
        self.clearInput.place(x=225, y=200)
        
        #reset data
        self.resetInput = customtkinter.CTkButton(master=self.appFrame, text="Reset Input", command=self.updateReturnLabel)
        self.resetInput.place(x=225, y=250)
        
        #converts the string text data to a list
        self.charConverterButton = customtkinter.CTkButton(master=self.appFrame, text='Format Data', command=self.convertTolist)
        self.charConverterButton.place(x=25, y=150)
        
        #applys a bubble sort to the list so it is now sorted alphabetically
        self.sortButton = customtkinter.CTkButton(master=self.appFrame, text='Sort Characters', command=self.Sort)
        self.sortButton.place(x=25, y=200)

        #button for displaying the mode of data
        self.dataModeButton = customtkinter.CTkButton(master=self.appFrame, text='Find Most Common Letter', command=self.dataMode)
        self.dataModeButton.place(x=25, y=250)
        
        #button for displaying the length of data
        self.lengthButton = customtkinter.CTkButton(master=self.appFrame, text="Length of Text", command=self.getLength)
        self.lengthButton.place(x=225, y=150)
        
        #BUTTONS

        #DEBUG
        if debug:
            self.invokeExceptButton = customtkinter.CTkButton(master=self.appFrame, text="Invoke Exception", command=self.invokeExcept)
            self.invokeExceptButton.place(x=425, y=300)
            
            self.resetScreenDimensions = customtkinter.CTkButton(master=self.appFrame, text='Reset Screen Dimensions', command=self.resetDims)
            self.resetScreenDimensions.place(x=400, y=300)
        #DEBUG
        
    def clearData(self) -> None:
        """
        Clears all data from the entry widget and resets the textData and input
        """
        
        self.textData = []
        self.updateReturnLabel()
        self.rawLength = 0
        
    def updateReturnLabel(self) -> None:
        """
        Used by methods and widgets in order to update the middle entry widget, removes previous data, inserts new data
        """
        
        self.labelReturn.delete(0, self.rawLength ** 2)
        self.labelReturn.insert(0, self.textData)
    
    def getLength(self) -> None:
        """
        Displays a message box onscreen of the length of the input file
        """
        
        messagebox.showinfo(title='Length', message=self.rawLength)
    
    def dataMode(self) -> None:
        """
        Displays the mode (most common letter found) in the text 
        """
        letterMode = statistics.mode(self.textData)
        messagebox.showinfo(title='Most Common Letter', message=letterMode)
        
    def convertTolist(self) -> None:
        """
        Fuction loops through all characters in the string and checks if it is in the alphabet (so no numbers, spaces, special characters etc.) 
        then re applys the new list to the current main one self.textData so its a list of all letters
        """
        
        textDataCONVERTED = []
        
        for element in self.textData:
            if element in self.Alphabet:
                if self.Alphabet.index(element) < 25:
                    textDataCONVERTED.append(element)
                else:
                    textDataCONVERTED.append(self.Alphabet[self.Alphabet.index(element)-26])
        self.textData = textDataCONVERTED
        self.updateReturnLabel()
        
    def Sort(self) -> None:
        """
        Python handles characters the same as integers so there is no need to work with integers and using just the characters will suffice
        Basic Bubble sort with n^2 complexity
        """
        
        data = self.textData
        for i in range(len(data)):
            for j in range(len(data)-1):
                if data[j] > data[j+1]:
                    _ = data[j]
                    data[j] = data[j+1]
                    data[j+1] = _
        self.textData = data
        self.updateReturnLabel()
    
    def invokeExcept(self):
        """
        For debugging purposes
        """
        raise Exception
    
    def resetDims(self) -> None:
        """
        Called when the dimensions need to be reset or just returned to default for debugging
        """
        
        self.geometry(self.defaultDimensions)
        
    def readFile(self, file) -> str:
        """
        Reads the file choosen in the option box on the GUI
        """
        
        try:
            textFileobj =open(file,"r")  #open input.txt and read
        except:
            messagebox.showerror(title="File Selection Error", message="Invalid File Please Try Again")
            return
        self.textData = textFileobj.read() #assign a variable to the data read
        textFileobj.close() #close the file, no longer needed since we have the data
        self.rawLength = len(self.textData)
        self.updateReturnLabel()
        
    def writeFile(self, file):
        """
        Writes the data into the file choosen in the option box on the GUI
        """
        
        #binary converter using pythons bult in functions
        if self.outputTypeBINARY.get() ==1:
            l,m=[],[]
            for i in self.textData:
                l.append(ord(i))
            for i in l:
                m.append(str(bin(i)[2:]))
            self.textData = m
        
        #convert to one concat string
        outputData = ''.join(self.textData)
        
        textFileobj =open(file, 'w')
        textFileobj.write(outputData)
        textFileobj.close()

if __name__ == '__main__':
    global version, debug
    debug:bool = settings.DEBUGSTATE()
    version:str = "1.4"
    app = App()
    app.mainloop()