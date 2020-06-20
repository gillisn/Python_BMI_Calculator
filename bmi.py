from sys import argv
import csv
import pandas as pd

class BMI:

    def __init__(self):
        self._stone=0
        self._pounds=0
        self._feet=0
        self._inches=0
        self._kgs=0
        self._cms=0

    def set_bmi_metric(self,kgs,cms):

        self.set_kgs(kgs)
        self.set_cms(cms)

    def set_bmi_imperial(self,stone,pounds,feet,inches):

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
        if  0 <= self.pounds <= 14:
            self.__pounds = pounds
        else:
            raise ValueError("Invalid pound value, there are 14 pounds in a stone.  You entered: %d" % pounds)

    def set_feet(self,feet):
        if 0 <= self.feet <= 9:
            self.__feet = feet
        else:
            raise ValueError("Invalid feet value, the tallest person ever recorded was under 9 feet and you entered: %d" % feet)

    def set_inches(self,inches):
        if 0 <= self.inches <= 12:
            self.__inches = inches
        else:
            raise ValueError("Invalid number of inches, there are 12 inches in a foot and you entered: %d" % inches)

    def set_kgs(self,kgs):
        if 0 <= self.kgs <= 500:
            self.__kgs = kgs
        else:
            raise ValueError("Invalid number of kgs, the heaviest person recorded was")

    def set_cms(self,cms):
        if 0 <= self.cms <= 300:
            self.__cms = cms
        else:
            raise ValueError("Invalid number of cms, the tallest person recorded was under 300cms and you entered: %d" %cms)

    def get_stone(self):
        return self.__stone

    def get_pounds(self):
        return self.__pounds

    def get_feet(self):
        return self.__feet

    def get_inches(self):
        return self.__inches

    def get_kgs(self):
        return self.__kgs

    def get_cms(self):
        return self.__cms

    def print_bmi_metric(self):
        print("%.2d:%.2d" % (self.__kgs,self.__cms))


    def metric_bmi(self):
        bmi_metric=""
        bmi_metric = self.__kgs/(self.__cms * self.__cms)
        print(bmi_metric)

    def imperial_bmi(self):
        bmi_imperial=""
        bmi_imperial = ((self.__stone*14)+self.__pounds) / ((self.__cms/100) * self.__cms/100) * 703
        print(bmi_imperial)

