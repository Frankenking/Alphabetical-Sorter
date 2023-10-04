import customtkinter
from tkinter import messagebox
import string
import os
import settings

class App(customtkinter.CTk):
    
    def __init__(self) -> None:
        super().__init__()
        
        #consts
        self.Alphabet = tuple(string.ascii_letters)
        print(self.Alphabet)
        #Vars
        
        #list to store data being modified
        self.textData:list = []
        
            #Dim Vars
        self.h, self.w = str(int(self.winfo_screenheight()/1.5)), str(int(self.winfo_screenwidth()/1.5)) # set variaible h(height) w(width) to 1.5 the native screen size
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
        self.mainlabel.place(x = 20, y = 50)
        
        self.labelReturn = customtkinter.CTkScrollableFrame(master=self.appFrame, label_text=" ", width=10,height= 0, orientation="horizontal")
        self.labelReturn.place(x=0, y= 50)
        
        self.dataOptionboxlabel = customtkinter.CTkLabel(master = self, text= "File Selection")
        self.dataOptionboxlabel.place(x=35, y=155)
        
        #LABELS
        
        #MISC
        self.dataOptionsboxVAR = customtkinter.StringVar(value='Select File')
        self.dataOptionsbox = customtkinter.CTkOptionMenu(master = self, values=os.listdir(), variable=self.dataOptionsboxVAR, command=self.readFile)
        self.dataOptionsbox.place(x = 20, y = 195)

        #MISC
        
        #BUTTONS 
        
        self.quitButton = customtkinter.CTkButton(master=self, text="Close App", command=self.quit)
        self.quitButton.place(x=20,y=250)
        
        #converts the string text data to a list
        self.charConverterButton = customtkinter.CTkButton(master=self.appFrame, text='Convert Data to List', command=self.convertTolist)
        self.charConverterButton.place(x=0, y=0)
        
        #applys a bubble sort to the list so it is now sorted alphabetically
        self.sortButton = customtkinter.CTkButton(master=self.appFrame, text='Sort Characters', command=self.Sort)
        self.sortButton.place(x=200, y=0)
    
        
        #BUTTONS

        #DEBUG
        if debug:
            self.invokeExceptButton = customtkinter.CTkButton(master=self.appFrame, text="Invoke Exception", command=self.invokeExcept)
            self.invokeExceptButton.place(x=425,y=50)
            
            self.resetScreenDimensions = customtkinter.CTkButton(master=self.appFrame, text='Reset Screen Dimensions', command=self.resetDims)
            self.resetScreenDimensions.place(x=425,y=0)
        #DEBUG
        
    def invokeExcept(self):
        raise Exception
    
    def updateReturnLabel(self) -> None:
        self.labelReturn.configure(label_text = f"{str(self.textData)}")
    
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
        Python handles ascii the same as binary so there is no need to work with integers and using just the characters will suffice
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
        
    def resetDims(self) -> None:
        """
        Called when the dimensions need to be reset or just returned to default
        """
        
        self.geometry(self.defaultDimensions)
        
    def readFile(self, file) -> str:
        
        textFileobj =open(file,"r")  #open input.txt and read
        self.textData = textFileobj.read() #assign a variable to the data read
        textFileobj.close() #close the file, no longer needed since we have the data
        self.updateReturnLabel()
        
    def writeFile(self):
        """
        Writes the data into the output.txt file
        """
        pass
    
if __name__ == '__main__':
    global version, debug
    debug:bool = settings.DEBUGSTATE()
    version:str = "0.0.7"
    program = App()
    program.mainloop()