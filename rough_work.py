#Nested Loops
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

#Lists
names = ['John','Bob','Sarah','Jack']
print(names[0])
print(names[1:3])

#Find the largest number in a list
numbers = [1,2,3,4,5,9,10]
print(max(numbers))

#2D Lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[2][1])

for row in matrix:
    for item in row:
        print(item)

#List methods
numbers = [4,5,3,2,9]
numbers.append(14)
numbers.insert(0,10)
numbers.remove(5)
numbers.clear()
print(numbers)

#Remove duplicates in a list
numbers = [1,2,1,2,3,4,3,2,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#Unpacking
coords = (1,2,3)
x,y,z = coords
print(x)
print(y)
#Dictionaries
customer = {
    "name":"John",
    "age":30,
    "is_verified":True
}
print(customer["name"])
print(customer.get("age "))

#Get user input and put into words
phone=input("Phone: ")
digits_mapping = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
output=""
for ch in phone:
    output += digits_mapping.get(ch,"!") + " "
print(output)