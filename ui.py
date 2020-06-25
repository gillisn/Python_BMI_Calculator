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

        BmiInterface(parent).grid(row=0, column=0)
        BmiInterface(parent).grid(row=0, column=1)

        # Add the Exit button
        ttk.Button(parent, text="Exit", command=parent.destroy).grid(row=1, column=1, sticky=tk.E, padx=15, pady=10)


class BmiInterface(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.bmi_props = BmiProperty()
        result = locale.setlocale(locale.LC_ALL, '')
        if result == 'C':
            locale.setlocale(locale.LC_ALL, 'en_US')

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

    # Display the grid of labels and text entry fields
    def initComponents(self):
        ttk.Label(self, text="Stone").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textVariable=self.stone).grid(column=1, row=0)

        ttk.Label(self, text="Feet").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textVariable=self.feet).grid(column=1, row=2)

        ttk.Label(self, text="Pounds").grid(column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=25, textVariable=self.pounds).grid(column=3, row=0)

        ttk.Label(self, text="Inches").grid(column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textVariable=self.inches).grid(column=3, row=0)

        ttk.Label(self, text="BMI Imperial:").grid(column=0, row=4, sticky=tk.E)
        ttk.Entry(self, width=25, textVariable=self.bmi_imperial, state="readonly").grid(column=1, row=0)

        ttk.Label(self, text="of KGs").grid(column=1, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textVariable=self.kgs).grid(column=4, row=0)

        ttk.Label(self, text="CM").grid(column=4, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textVariable=self.cms).grid(column=4, row=0)

        ttk.Label(self, text="BMI Metric:").grid(column=1, row=2, sticky=tk.E)
        ttk.Entry(self, width=25, textVariable=self.bmi_metric, state="readonly").grid(column=1, row=0)

        self.makeButtons()

        for child in self.winfo_children():
            child._grid_configure(padx=5, pady=3)

    def makeButtons(self):
        buttonFrame = ttk.Frame(self)
        buttonFrame.grid(column=0, row=5, columnspan=2, sticky=tk.E)

        ttk.Button(buttonFrame, text="Clear", command=self.clear).grid(column=0, row=5, padx=5)
        ttk.Button(buttonFrame, text="Calculate BMI", command=self.calculate).grid(column=1, row=5, padx=5)

    def calculate(self):
        self.bmi_props._stone = int(self.stone.get())
        self.bmi_props._pounds = int(self.pounds.get())
        self.bmi_props._feet = int(self.feet.get())
        self.bmi_props._inches = int(self.inches.get())

        self.bmi_props._kgs = float(self.kgs.get())
        self.bmi_props._cms = float(self.cms.get())

        self.bmi_metric.set(self.bmi_props.metric_bmi())
        self.bmi_imperial.set(self.bmi_props.imperial_bmi())

    def clear(self):
        self.stone.set("")
        self.pounds.set("")
        self.feet.set("")
        self.inches.set("")
        self.kgs.set("")
        self.cms.set("")
        self.bmi_metric.set("")
        self.bmi_imperial.set("")


if __name__ == " main ":
    root = tk.Tk()
    #root.geometry("400x400")
    #root.resizable(width=False,height=False)
    root.title("BMI Calculator")
    BmiInterfaces(root)
    root.mainloop()
