#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import locale

from business import Investment

class FutureValueFrames(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        # Add the FutureValueFrames
        FutureValueFrame(parent).grid(row=0, column=0)
        #FutureValueFrame(parent).grid(row=1, column=5)
        #FutureValueFrame(parent).grid(row=1, column=6)

        # Add the Exit button        
        ttk.Button(parent, text="Exit", command=parent.destroy).grid(
            row=1, column=1, sticky=tk.E, padx=15, pady=10)

class FutureValueFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.investment = Investment()
        result = locale.setlocale(locale.LC_ALL, '')
        if result == 'C':
            locale.setlocale(locale.LC_ALL, 'en_US')


        # dependent project
        # Define string variables for text entry fields
        self.monthlyInvestment = tk.StringVar()
        self.yearlyInterestRate = tk.StringVar()
        self.years = tk.StringVar()
        self.futureValue = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        # change with project
        # Display the grid of labels and text entry fields
        ttk.Label(self, text="Enter your Weight").grid(
            column=3, row=0, sticky=tk.E)

        ttk.Label(self, text="Stones:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.monthlyInvestment).grid(
            column=1, row=1)

        ttk.Label(self, text="Pounds:").grid(
            column=2, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.yearlyInterestRate).grid(
            column=3, row=1)

        ttk.Label(self, text="or KGs:").grid(
            column=4, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.years).grid(
            column=5, row=1)

        ttk.Label(self, text="Enter your Height").grid(
            column=3, row=2, sticky=tk.E)

        ttk.Label(self, text="Feet:").grid(
            column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.years).grid(
            column=1, row=3)

        ttk.Label(self, text="Inches:").grid(
            column=2, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.years).grid(
            column=3, row=3)

        ttk.Label(self, text="or CM:").grid(
            column=4, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.years).grid(
            column=5, row=3)


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

        ttk.Button(buttonFrame, text="Calculate Your BMI Now, Motherfucker!!", command=self.calculate) \
            .grid(column=1, row=0)

        ttk.Button(buttonFrame, text="Clear", command=self.clear) \
            .grid(column=2, row=0 , padx=5)

    def calculate(self):
        self.investment.monthlyInvestment = float(
            self.monthlyInvestment.get())
        self.investment.yearlyInterestRate = float(
            self.yearlyInterestRate.get())
        self.investment.years = int(
            self.years.get())

        self.futureValue.set(locale.currency(
                self.investment.calculateFutureValue(), grouping=True))

    def clear(self):
        # changes with project
        self.monthlyInvestment.set("")
        self.yearlyInterestRate.set("")
        self.years.set("")
        self.futureValue.set("")
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Future Value Calculator")
    FutureValueFrames(root)
    root.mainloop()
