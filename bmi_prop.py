#Name: Naoimi Gillis
#Email: gillisnaoimi5@gmail.com
#Phone: 0857227932

from sys import argv
import csv
import pandas as pd

class BmiProperty:

    def __init__(self,stone=0,pounds=0,feet=0,inches=0,kgs=89,cms=170):
        self.set_imp_inputs(stone,pounds,feet,inches)
        self.set_metric_inputs(kgs, cms)

    def set_metric_inputs(self,kgs,cms):
        self.kgs = kgs
        self.cms = cms

    def set_imp_inputs(self,stone,pounds,feet,inches):
        self.stone = stone
        self.pounds = pounds
        self.feet = feet
        self.inches = inches

    @property
    def kgs(self):
        return self.__kgs

    @kgs.setter
    def kgs(self,kgs):
        if 0 <= kgs <= 500:
            self.__kgs=kgs
        else:
            raise ValueError("Invalid kgs value: " % kgs)

    @property
    def cms(self):
        return self.__cms

    @cms.setter
    def cms(self,cms):
        if 0 <= cms <= 300:
            self.__cms=cms
        else:
            raise ValueError("Invalid cms value: " % cms)

    @property
    def stone(self):
        return self.__stone

    @stone.setter
    def stone(self,stone):
        if 0 <= stone <= 70:
            self.__stone=stone
        else:
            raise ValueError("Invalid stones value: " % stone)

    @property
    def pounds(self):
        return self.__pounds

    @pounds.setter
    def pounds(self,pounds):
        if 0 <= pounds <= 14:
            self.__pounds=pounds
        else:
            raise ValueError("Invalid pounds value: " % pounds)

    @property
    def feet(self):
        return self.__feet

    @feet.setter
    def feet(self,feet):
        if 0 <= feet <= 9:
            self.__feet=feet
        else:
            raise ValueError("Invalid feet value: " % feet)

    @property
    def inches(self):
        return self.__inches

    @inches.setter
    def inches(self,inches):
        if 0 <= inches <= 14:
            self.__inches=inches
        else:
            raise ValueError("Invalid inches value: " % inches)

    def print_bmi_metric(self):
        print("Your BMI Metric inputs are: " "%.2d:%.2d" % (self.kgs,self.cms))

    def print_bmi_imperial(self):
        print("Your BMI Imperial inputs are: "" %.2d:%.2d%.2d:%.2d" % (self.stone,self.pounds,self.feet,self.inches))

    def metric_bmi(self):
        bmi=""
        bmi = self.kgs/(self.cms * self.cms)*10000
        return bmi

    def imperial_bmi(self):
        bmi=""
        bmi = (((self.stone*14)+self.pounds)*703) / (((self.feet*12)+self.inches)**2)
        return bmi

    # Need a reference table here to add the bmi status into dataframe
    #This bit does not work unless I hard code values
    '''bmi=0
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
    '''

    #Save results to a dataframe
    #This bit works when I hard code
    '''
    df = pd.DataFrame(columns=['Stone','Pounds','Feet','Inches','Kgs','Cms','BMI','BMI Status'])
    df1 = pd.DataFrame(data=[[stone,pounds,feet,inches,kgs,cms,bmi,bmi_status(bmi)]],
                       columns=['Stone','Pounds','Feet','Inches','Kgs','Cms',"BMI","BMI Status"])
    df = pd.concat([df, df1], axis=0)
    print(df)
    '''

    # Save results to a csv
    #This bit works when I hard code it
    '''df.to_csv('filename.csv', sep='\t')'''