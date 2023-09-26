import customtkinter
from tkinter import messagebox
import string

class App(customtkinter.CTk):
    
    def __init__(self) -> None:
        super().__init__()
        
        #CONSTs
        self.Alphabet = list(string.ascii_lowercase)
        #Vars
        
            #Dim Vars
        h, w = str(int(self.winfo_screenheight()/2)), str(int(self.winfo_screenwidth()/2)) # set variaible h(height) w(width) to half the native screen size
        self.defaultDimensions = w + "x" + h #make a string compatible with the tkinter geometry() function
        
            #Key Dictionary for Data Conversion
        self.letterKey = {}

            #Converted List
        self.textDataCONVERTED = []
        
        #Obtain the data convert to array/list
        self.textData = self.readFile()
        self.textData = [*self.textData.lower()]
        
        #Generate dictionary
        self.generateKey()
        
        #Startup GUI/Interfacing Functions
        
            #title
        self.title("Alphabetical Sorter")
        
            #apply previous dimensions
        self.resetDims()
        
            #appFrame to container widgets
        self.appFrame = customtkinter.CTkFrame(master=self)
        self.appFrame.pack(pady = 25, padx = 60, fill="both", expand=True)
    

        #Converter char->int
        self.charConverter()
        print(self.textDataCONVERTED)
        
        #Hybrid Quicksort, Quicksort/Insertion Sort
        
    
    def charConverter(self) -> None:
        for element in self.textData:
            if element in self.Alphabet:
                self.textDataCONVERTED.append(self.letterKey[element])
            else:
                self.textDataCONVERTED.append(" ")
                
    def generateKey(self) -> None:
        count = 0
        for letter in self.Alphabet:
            self.letterKey.update({letter:count})
            count +=1
        self.letterKey.update({" ":26})
    
    def hybridSort(self) -> list:
        pass
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