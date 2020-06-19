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