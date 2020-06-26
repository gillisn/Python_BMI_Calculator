#Name: Naoimi Gillis
#Email: gillisnaoimi5@gmail.com
#Phone: 0857227932

import tkinter as tk
from tkinter import ttk
import locale

from bmi_prop import BmiProperty

class BmiInterfaces(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        # Add the FutureValueFrames
        BmiFrame(parent).grid(row=0, column=0)
        # BmiFrame(parent).grid(row=1, column=5)
        # BmiFrame(parent).grid(row=1, column=6)

        # Add the Exit button
        ttk.Button(parent, text="Exit", command=parent.destroy).grid(row=1, column=1, sticky=tk.E, padx=15, pady=10)


class BmiFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.bmi_props = BmiProperty()
        result = locale.setlocale(locale.LC_ALL, '')
        if result == 'C':
            locale.setlocale(locale.LC_ALL, 'en_US')

        # dependent project
        # Define string variables for text entry fields
        # Define string variables for text entry fields
        self.stone = tk.StringVar()
        self.pounds = tk.StringVar()
        self.feet = tk.StringVar()
        self.inches = tk.StringVar()
        self.kgs = tk.StringVar()
        self.cms = tk.StringVar()
        self.bmi_metric = tk.StringVar()
        self.bmi_imperial = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        # change with project
        # Display the grid of labels and text entry fields
        ttk.Label(self, text="Enter your Weight").grid(column=3, row=0, sticky=tk.E)

        ttk.Label(self, text="Stones:").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.stone).grid(column=1, row=1)

        ttk.Label(self, text="Pounds:").grid(column=2, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.pounds).grid(column=3, row=1)

        ttk.Label(self, text="or KGs:").grid(column=4, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.kgs).grid(column=5, row=1)

        ttk.Label(self, text="Enter your Height").grid(column=3, row=2, sticky=tk.E)

        ttk.Label(self, text="Feet:").grid(column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.feet).grid(column=1, row=3)

        ttk.Label(self, text="Inches:").grid(column=2, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.inches).grid(column=3, row=3)

        ttk.Label(self, text="or CM:").grid(column=4, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.cms).grid(column=5, row=3)

        ttk.Label(self, text="BMI Results").grid(column=0, row=4, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.bmi_metric,state="readonly").grid(column=1, row=4)

        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons(self):
        # stays same
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=1, row=4, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(self, width=25, text="Calculate your BMI", command=self.calculate).grid(column=1, row=5)
        ttk.Button(buttonFrame, text="Clear", command=self.clear).grid(column=4, row=5)

    def calculate(self):
        self.bmi_metric.set(self.bmi_props.metric_bmi())

    def clear(self):
        self.stone.set("")
        self.pounds.set("")
        self.feet.set("")
        self.inches.set("")
        self.kgs.set("")
        self.cms.set("")
        self.bmi_metric.set("")
        self.bmi_imperial.set("")

#Add in exception handling for the inputs
''' goagain=True
    while(goagain==True):
        try:
            stone = int(input("Enter your weight in stone: "))
            pounds = int(input("Enter your pounds of weight(no more than 14 pounds in a stone): "))
            feet = int(input("Enter your height in feet: "))
            inches = int(input("Enter your inches of height(no more than 12 inches in a foot): "))
            kgs = float(input("Enter your weight in kgs: "))
            cms = float(input("Enter your height in cms: "))
            metric_check=kgs/cms
            goagain=False
        except ValueError:
            print("Decimals only for kgs and cms.  Whole numbers only for stone, pounds, feet, inches")
        except ZeroDivisionError:
            print("Cannot divide by zero")
        else:
            print("Works")
            goagain=False

    print("It works")
'''

if __name__ == "__main__":
    root = tk.Tk()
    root.title("BMI Calculator")
    BmiInterfaces(root)
    root.mainloop()