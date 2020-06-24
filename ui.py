import tkinter as tk
from tkinter import ttk
import locale
from bmi import Bmi

class BmiInterfaces(ttk.Frame):
    def __init__(self,parent):
        ttk.Frame.__init__(self,parent)

        BmiInterface(parent).grid(row=0,column=0)
        BmiInterface(parent).grid(row=0,column=0)

        #Add the Calculate button
        ttk.Button(parent,text="Calculate",command=parent.destroy).grid(row=1,column=1,sticky=tk.E,padx=15,pady=10)

class BmiInterface(ttk.Frame):
    def __init__(self,parent):
        ttk.Frame.__init__(self,parent,padding="10 10 10 10")
        self.parent = parent
        self.bmi= BMI()
        result=locale.setlocale(locale.LC_ALL,'en_US')

        #Define string variables for text entry fields
        self.stone=tk.StringVar()
        self.pounds=tk.StringVar()
        self.feet=tk.StringVar()
        self.inches=tk.StringVar()
        self.kgs=tk.StringVar()
        self.cms=tk.StringVar()

        self.initComponents()

    # Display the grid of labels and text entry fields
    def initComponents(self):
        ttk.Label(self,text="Stone").grid(column=0,row=0,sticky=tk.E)
        ttk.Entry(self,width=25,textVariable=self.stone).grid(column=1,row=0)

        ttk.Label(self, text="Feet").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textVariable=self.feet).grid(column=1, row=2)

        ttk.Label(self, text="Pounds").grid(column=2, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textVariable=self.pounds).grid(column=3, row=0)

        ttk.Label(self, text="Inches").grid(column=3, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textVariable=self.inches).grid(column=3, row=0)

        ttk.Label(self, text="of KGs").grid(column=4, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textVariable=self.kgs).grid(column=4, row=0)

        ttk.Label(self, text="CM").grid(column=4, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textVariable=self.cms).grid(column=4, row=0)

        self.makeButtons()

        for child in self.winfo_children():
            child._grid_configure(padx=5,pady=3)

    def makeButtons(self):
        buttonFrame=ttk.Frame(self)
        buttonFrame.grid(column=4,row=6,columnspan=2,sticky=tk.E)
        ttk.Button(buttonFrame,text="Clear", command=self.clear).grid(column=0,row=0,padx=5)
        ttk.Button(buttonFrame, text="Caluclate your BMI", command=self.calculate).grid(column=1, row=0, padx=5)


    def calculate(self):
        self.bmi._stone=float(self.stone.get())
        self.bmi._pounds = float(self.pounds.get())
        self.bmi._feet=float(self.feet.get())
        self.bmi._inches = float(self.inches.get())
        self.bmi._kgs = float(self.kgs.get())
        self.bmi._cms = float(self.cms.get())

    def clear(self):
        self.stone.set("")
        self.pounds.set("")
        self.feet.set("")
        self.inches.set("")
        self.kgs.set("")
        self.cms.set("")

if __name__ == " main ":
    root = tk.Tk
    root.title("BMI Calculator")
    BmiInterfaces(root)
    root.mainloop()