#Name: Naoimi Gillis
#Email: gillisnaoimi5@gmail.com
#Phone: 0857227932
#Roughwork

from sys import argv
import csv
import pandas as pd

#Define empty variables
name = ()
height = ()
weight = ()
units = ()
bmi = ()
bmi_status = ()

'''
#Get user inputs 
name = input("Enter your name: ")
height = float(input("Enter your height: "))/100
weight = float(input("Enter your weight: "))
#units =
'''

#Need a reference table here to add the bmi status into dataframe
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


#Depending on units open an if statement, metric down one rabbit hole
def BMI(name,units,weight,height):
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
print("Hello %s, your BMI is %.2f" % (name,bmi))
'''
print("Hello %s, your weight is %.2f kilograms, your height is %.2f metres, your BMI is %.2f" % (name,weight,height,bmi))

#Calculate your BMI on Metric.  BMI = weight in kgs/(height in metres * height in metres)
def bmiMetric(height,weight):
    bmi = weight/(height*height)
    return(bmi)

bmi = bmiMetric(height,weight)
print(bmi)

#Convert values for Imperial to pounds and inches
height_inches = (feet*12)+inches
weight_pounds = (stone*14)+pounds

#Calculate your BMI on Imperial.  BMI = weight in pounds/(height in inches*height in inches)*703
print("Hello %s, your weight is %.2f kilograms, your height is %.2f metres, your BMI is %.2f" % (name,weight,height,bmi))
def bmiImperial(height,weight):
    bmi=weight/(height*height)*703
    return(bmi)
'''
'''
#Save results to a dataframe
df = pd.DataFrame(columns=['Name','Weight','Height','BMI','BMI Status'])
df1 = pd.DataFrame(data=[[name,weight,height,bmi,bmi_status(bmi)]],columns=["Name","Weight","Height","BMI","BMI Status"])
df=pd.concat([df,df1],axis=0)

print(df)

#Save results to a csv
df.to_csv('filename.csv',sep='\t')

'''

'''#Enter your Name
print("Welcome to this BMI Calculator.")
name = input("Please enter your name: ")
print(name)

#Check the type of the name
print(type(name))

#Define  weight and height variables for metric and get input
height = float(input("Please enter your height: "))
weight = float(input("Please enter your weight: "))

print(type(weight))
print(weight)
print(height)

#Convert centimetres to metres.  CMs/100
height = height/100

#Decide on Imperial or Metric Inputs
print("Do you want to use imperial units? Yes or No.  If you select Yes you get Imperial, if you select No then Metrics")
units = bool(input("Imperial units? Yes or no"))
print(type(units))

#If imperial then enter your weight and height

#Check for Errors with inputs, are they numeric, an  integer, not a float

#Convert Imperial weight to pounds.  (Stone inputted)*14 + pounds inputted = Pounds

#Convert Imperial height to inches.  (Feet inputted)*12 + inches inputted = Inches

#Calculate your BMI on Imperial.  BMI = (Imp Weight in pounds / (height in inches * height in inches))*703

#If Metric then enter your weight and height

#Check for errors with inputs, allow floats and integers for both centimetres and kgs

#Convert centimetres to metres.  CMs/100

#Calculate your BMI on Metric.  BMI = weight in kgs/(height in metres * height in metres)

#Save output to csv file'''

#Name: Naoimi Gillis
#Email: gillisnaoimi5@gmail.com
#Phone: 0857227932
#Roughwork

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
        self._kgs=57
        self._cms=164

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
    bmi=0.0
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
    def bmi(name, units):
        name = input("Please type your name: ")
        units = input("Please type units - METRIC or IMPERIAL? ").upper()

        if units == "METRIC":
            def metric_bmi(self):
                bmi_metric = ""
                bmi_metric = self._kgs / (self._cms * self._cms) * 10000
                print(bmi_metric)

        elif units == "IMPERIAL":
            def imperial_bmi(self):
                bmi_imperial = ""
                bmi_imperial = (((self._stone * 14) + self._pounds) * 703) / (((self._feet * 12) + self._inches) ** 2)
                print(bmi_imperial)
        else:
            print("Did you spell it correctly?")

#print("Hello %s, your BMI is %.2f" % (name, bmi))
