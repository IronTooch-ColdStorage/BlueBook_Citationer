import tkinter as tk
from mainWindow import MainWindow

myMainWindow = MainWindow()

class MainPage():
    def __init__(self):
        self.root = tk.Tk()
        
    def run(self):
        myMainWindow.DrawMainWindow(tkRoot = self.root)  
        self.autorefresh()
        self.root.mainloop()

    def autorefresh(self):
        myMainWindow.ProcessUpdates(tkRoot = self.root)  
        self.root.after(500,self.autorefresh)
	
	
if __name__ == '__main__':
    m = MainPage()
    m.run()
	
mainPage = MainPage()