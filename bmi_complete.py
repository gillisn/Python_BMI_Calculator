#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import locale

from bmi_prop import BmiProperty


class FutureValueFrames(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        # Add the FutureValueFrames
        FutureValueFrame(parent).grid(row=0, column=0)
        # FutureValueFrame(parent).grid(row=1, column=5)
        # FutureValueFrame(parent).grid(row=1, column=6)

        # Add the Exit button
        ttk.Button(parent, text="Exit", command=parent.destroy).grid(row=1, column=1, sticky=tk.E, padx=15, pady=10)


class FutureValueFrame(ttk.Frame):
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

        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons(self):
        # stays same
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=2, row=4, columnspan=1, sticky=tk.E)

        # Add two buttons to the button frame

        ttk.Button(buttonFrame, text="Calculate Your BMI Now, Motherfucker!!") \
            .grid(column=1, row=0)

        ttk.Label(self, text="BMI Results:").grid(column=0, row=5, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.calculate,state="readonly").grid(column=1, row=5)

        ttk.Button(buttonFrame, text="Clear", command=self.clear).grid(column=2, row=0, padx=5)

    def calculate(self):
        self.bmi_props._stone = int(self.stone.get())
        self.bmi_props._pounds = int(self.pounds.get())
        self.bmi_props._feet = int(self.feet.get())
        self.bmi_props._inches = int(self.inches.get())

        self.bmi_props._kgs = float(self.kgs.get())
        self.bmi_props._cms = float(self.cms.get())

        # self.bmi_metric = self.bmi_props.metric_bmi()
        self.bmi_metric.set(self.bmi_props.metric_bmi())
        #self.bmi_imperial.set(self.bmi_props.imperial_bmi())

    def clear(self):
        self.stone.set("")
        self.pounds.set("")
        self.feet.set("")
        self.inches.set("")
        self.kgs.set("")
        self.cms.set("")
        self.bmi_metric.set("")
        self.bmi_imperial.set("")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Future Value Calculator")
    FutureValueFrames(root)
    root.mainloop()
