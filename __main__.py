import customtkinter
from tkinter import messagebox
import string

class App(customtkinter.CTk):
    
    def __init__(self) -> None:
        super().__init__()
        
        #All for Tkinter interface startup
        
        #Vars
        
            #Dim Vars
        h, w = str(int(self.winfo_screenheight()/2)), str(int(self.winfo_screenwidth()/2)) # set variaible h(height) w(width) to half the native screen size
        self.defaultDimensions = w + "x" + h #make a string compatible with the tkinter geometry() function
        
        #Startup GUI/Interfacing Functions
        
            #title
        self.title("Alphabetical Sorter")
        
            #apply previous dimensions
        self.resetDims()
        
            #appFrame to container widgets
        self.tempbutton = customtkinter.CTkButton(master=self)
        self.tempbutton.place(x = 20, y = 50)
        
        self.appFrame = customtkinter.CTkFrame(master=self)
        self.appFrame.pack(pady = 45, padx = 175, fill="both", expand=True)
        
        self.dataTextbox = customtkinter.CTkLabel(master = self.appFrame, width=5,height=5,text="test")
        self.dataTextbox.place(x = 0, y = 0)
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
        
    def charConverter(self, ) -> list:
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
    program = App()
    program.mainloop()