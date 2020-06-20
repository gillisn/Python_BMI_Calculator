from sys import argv
import csv
import pandas as pd

class BMI:

    def __init__(self):
        #Imperial units initialised to zero
        self.stone = 0
        self.pounds = 0
        self.feet = 0
        self.inches = 0
        #Metric Units intialised to zero
        self.kgs = 57
        self.cms = 164

    def set_inputs(self,stone,pounds,feet,inches,kgs,cms):

        self.set_stone(stone)
        self.set_pounds(pounds)
        self.set_feet(feet)
        self.set_inches(inches)
        self.set_kgs(kgs)
        self.set_cms(cms)

    def set_stone(self,stone):
        if 0 <= stone < 70:
            self._stone = stone
        else:
            raise ValueError("Invalid stone value, the heaviest person ever recorded was 69 stone and you entered: %d" % stone)

    def set_pound(self,pounds):
        if  0 <= self._pounds <= 14:
            self._pounds = pounds
        else:
            raise ValueError("Invalid pound value, there are 14 pounds in a stone.  You entered: %d" % pounds)

    def set_feet(self,feet):
        if 0 <= self._feet <= 9:
            self._feet = feet
        else:
            raise ValueError("Invalid feet value, the tallest person ever recorded was under 9 feet and you entered: %d" % feet)

    def set_inches(self,inches):
        if 0 <= self._inches <= 12:
            self._inches = inches
        else:
            raise ValueError("Invalid number of inches, there are 12 inches in a foot and you entered: %d" % inches)

    def set_kgs(self,kgs):
        if 0 <= self._kgs <= 500:
            self._kgs = kgs
        else:
            raise ValueError("Invalid number of kgs, the heaviest person recorded was")

    def set_cms(self,cms):
        if 0 <= self._cms <= 300:
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
        print("%.2d:%.2d" % (self._kgs,self._cms))


    def metric_bmi(self,kgs,cms):
        self.bmi = self.kgs/(self.cms * self.cms)
        return (self.bmi)


    def imperial_bmi(self):
        self.bmi = ((self.stone*14)+self.pounds) / ((self.cms/100) * self.cms/100) * 703
        return (bmi)


