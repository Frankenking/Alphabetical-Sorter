import customtkinter
from tkinter import messagebox
import string
import os

class App(customtkinter.CTk):
    
    def __init__(self) -> None:
        super().__init__()
        
        #All for Tkinter interface startup
        
        #Vars
        
            #Dim Vars
        h, w = str(int(self.winfo_screenheight()/1.5)), str(int(self.winfo_screenwidth()/1.5)) # set variaible h(height) w(width) to half the native screen size
        self.defaultDimensions = w + "x" + h #make a string compatible with the tkinter geometry() function
        
        #Startup GUI/Interfacing Functions
        
            #title
        self.title("Alphabetical Sorter")
        
            #apply previous dimensions
        self.resetDims()
        
            #appFrame to container 
        self.mainlabel = customtkinter.CTkLabel(master=self, width=8,height=5,text=f"TextConverter & Sorter \nversion{version}\n artyom curtis")
        self.mainlabel.place(x = 20, y = 50)
        
        self.appFrame = customtkinter.CTkFrame(master=self)
        self.appFrame.pack(pady = 45, padx = 175, fill="both", expand=True)
        
        self.dataTextboxlabel = customtkinter.CTkLabel(master = self, text= "File Selection")
        self.dataTextboxlabel.place(x=35, y=155)
        
        self.dataTextbox = customtkinter.CTkOptionMenu(master = self, values=os.listdir())
        self.dataTextbox.place(x = 20, y = 195)
        self.main()

    def main(self) -> None:
        
        #CONSTs
        self.Alphabet = tuple(string.ascii_lowercase)
        
        #Generate dictionary
        self.letterKey:dict = {}
        self.numberKey:dict = {}
        self.generateKeys()
        
        #obtain data
        self.textData = self.readFile()
        self.textData = [*self.textData.lower()]
        
        #Converter char->int
        self.textData = self.charConverter()
        print(self.textData)
        
        #Hybrid Quicksort, Quicksort/Insertion Sort
        self.textData = self.bubbleSort(self.textData)
        print(self.textData)
        
        self.textData = self.numConverter()
        print(self.textData)
        
    def charConverter(self) -> list:
        textDataCONVERTED = []
        for element in self.textData:
            if element in self.Alphabet:
                textDataCONVERTED.append(self.letterKey[element])
        return textDataCONVERTED
    
    def numConverter(self) -> list:
        textDataCONVERTED = []
        for element in self.textData:
                textDataCONVERTED.append(self.numberKey[element])
        return textDataCONVERTED
    
    def generateKeys(self) -> None:
        count = 0
        for letter in self.Alphabet:
            self.letterKey.update({letter:count})
            self.numberKey.update({count:letter})
            count +=1
            
    def bubbleSort(self, data):
        
        for i in range(len(data)):
            for j in range(len(data)-1):
                if data[j] > data[j+1]:
                    temp = data[j]
                    data[j] = data[j+1]
                    data[j+1] = temp
        return data
    
    def resetDims(self) -> None:
        self.geometry(self.defaultDimensions)
        
    def readFile(self) -> str:
        
        textFileobj =open(r"input.txt","r")  #open input.txt
        data = textFileobj.read() #assign a variable to the data
        textFileobj.close() #close the file, no longer needed since we have the data
        return data
    
    def writeFile(self):
        pass
    
if __name__ == '__main__':
    global version
    version:str = "0.0.3"
    program = App()
    program.mainloop()