#Name: Naoimi Gillis
#Email: gillisnaoimi5@gmail.com
#Phone: 0857227932
#Attempt 2

from sys import argv
import csv
import pandas as pd

class Bmi:

    #Constructor
    def __init__(self):
        self._stone=1
        self._pounds=1
        self._feet=1
        self._inches=1
        self._kgs=1
        self._cms=1
        self.bmi=0

    def set_metric_inputs(self,kgs,cms):
        self.set_kgs(kgs)
        self.set_cms(cms)

    def set_imp_inputs(self,stone,pounds,feet,inches):
        self.set_stone(stone)
        self.set_pounds(pounds)
        self.set_feet(feet)
        self.set_inches(inches)


    def set_stone(self,stone):
        if 0 <= stone < 70:
            self._stone = stone
        else:
            raise ValueError("Invalid stone value, the heaviest person ever recorded was 69 stone and you entered: %d" % stone)

    def set_pound(self,pounds):
        if  0 <= pounds <= 14:
            self._pounds = pounds
        else:
            raise ValueError("Invalid pound value, there are 14 pounds in a stone.  You entered: %d" % pounds)

    def set_feet(self,feet):
        if 0 <= feet <= 9:
            self._feet = feet
        else:
            raise ValueError("Invalid feet value, the tallest person ever recorded was under 9 feet and you entered: %d" % feet)

    def set_inches(self,inches):
        if 0 <= inches <= 12:
            self._inches = inches
        else:
            raise ValueError("Invalid number of inches, there are 12 inches in a foot and you entered: %d" % inches)

    def set_kgs(self,kgs):
        if 0 <= kgs <= 500:
            self._kgs = kgs
        else:
            raise ValueError("Invalid number of kgs, the heaviest person recorded was")

    def set_cms(self,cms):
        if 0 <= cms <= 300:
            self._cms = cms
        else:
            raise ValueError("Invalid number of cms, the tallest person recorded was under 300cms and you entered: %d" %cms)

    def get_stone(self):
        return self._stone

    def get_pounds(self):
        return self._pounds

    def get_feet(self):
        return self._feet

    def get_inches(self):
        return self._inches

    def get_kgs(self):
        return self._kgs

    def get_cms(self):
        return self._cms

    def print_bmi_metric(self):
        print("Your BMI Metric inputs are: " "%.2d:%.2d" % (self._kgs,self._cms))

    def print_bmi_imperial(self):
        print("Your BMI Imperial inputs are: "" %.2d:%.2d%.2d:%.2d" % (self._stone,self._pounds,self._feet,self._inches))

    def metric_bmi(self):
        bmi_metric=""
        bmi_metric = self._kgs/(self._cms * self._cms)*10000
        print(bmi_metric)

    def imperial_bmi(self):
        bmi_imperial=""
        bmi_imperial = (((self._stone*14)+self._pounds)*703) / (((self._feet*12)+self._inches)**2)
        print(bmi_imperial)

    # Need a reference table here to add the bmi status into dataframe
    bmi=0
    def bmi_status(bmi):
        if bmi < 18.5:
            return "Underweight BMI"
        elif 18.501 <= bmi < 24.5:
            return "Healthy weight"
        elif 24.501 <= bmi < 29.9:
            return "Overweight"
        elif 29.901 <= bmi < 250:
            return "Obese"
        else:
            raise ValueError('Unsupported BMI: {}'.format(bmi))

    # Depending on units open an if statement, metric down one rabbit hole
    name=""
    def BMI(name, units, weight, height):
        name = input("Please type your name: ")
        units = input("Please type units - METRIC or IMPERIAL? ").upper()
        weight = float(input("weight: "))
        height = float(input("height: "))

        if units == "METRIC":
            bmi = weight / (height * height)
            return bmi

        elif units == "IMPERIAL":
            bmi = (weight * 703) / (height * height)
            return bmi
        else:
            print("Did you spell it correctly?")

    bmi_status(bmi)
    print("Hello %s, your BMI is %.2f" % (name, bmi))
