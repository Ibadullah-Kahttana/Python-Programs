
print("Hello World")

number = 1
number2 = 10
print("Number 1 =", number, ", Number 2 = ",
      number2, ", Addition = ", number+number2)

a, b, c = 5, 3.2, 'Hello'

print(a)  # prints 5
print(b)  # prints 3.2
print(c)  # prints Hello

patient_name = "John Smith"
age = 20
is_patient = True

print("Patient Name is", patient_name , ", His age is ",age, "and, He is serious", is_patient)

"""Input"""

patient_name = input("Patient Name ? ")
age = input("Patient AGE ? ")
is_patient = input("Recovered ? ")

print("Patient Name is", patient_name, ", His age is ",
      age, "and, He is serious", is_patient)

"""Type Conversion

int()
float()
str()
bool() 
"""

first_num = input("Num 1 = " )
second_num = input("Num 2 = " ) 

'''
ALSO

first_num = float(input("Num 1 = " ))
second_num = float(input("Num 2 = " )) 
sum = first_num + second_num

'''

sum = float(first_num) + float(second_num)
print("Sum = " + str(sum))

"""Strings ( & Capabilties or methods)

replace()
upper()
capitalized()
casefold()
center()
count()
encode()
endswith()
expandtabs()

"""

string = str(input("Enter a String : "))
print("Replace(par1 , par2) : ", string.replace("ullah" , "Kahttana"))
print("Upper() : ", string.upper())
print("Lower() : ", string.lower())
print("Find() : ", string.find("a"))
print("In : ", "Ibad" in string )

"""Python Namespace and Scope
Global() 
Outer()
Inner()
"""

# global_var is in the global namespace
global_var = 10
def outer_function():
    #  outer_var is in the local namespace 
    outer_var = 20
    def inner_function():
        #  inner_var is in the nested local namespace 
        inner_var = 30
        print(inner_var)
    print(outer_var)
    inner_function()

# print the value of the global variable
print(global_var)

# call the outer function and print local and nested local variables
outer_function()

dict_weather = { 'Monday' : 'cloudy' ,'Tuesday' : 'sunny' ,'Wednesday' : 'PartialyCloudy' ,'Thursday' : 'PartialyCloudy' ,'Friday' : 'WetWeather' ,'Saturday' : 'cloudy' , 'Sunday' : 'Sunny' }

PredictWeather = dict_weather['Monday']
print(PredictWeather)

#dictionary sortes
customers = ['Kaley Fernandez', 'Darius Rowland', 'Isaac Borthwick',  'Alexandria Kidd']
sorted_customers = sorted(customers)
print(sorted_customers)

print("Sorted Dict" , sorted(dict_weather))

"""BMI Example <br>
round()
upper()
"""

weight = float (input("Weight: "))
unit = input("(K)g or (Lbs):")
if unit.upper() == "K":
  converted = weight/0.45
  print("Weight in kgs:", round(converted,1))
elif unit.upper() == "L":
  converted = weight * 0.45
  print("Weight in lbs:", round(converted,1))

"""While Loop"""

'''we can multiply a number by a string  ( 1 * 'a') correct
   but we cannot concatinate a number with a string (1 + 'a') wrong '''
i = 1
while i<5:
  print(i * 2 * '*')   
  i = i+1

"""**Multiplicatin Table**
Uisng for loop
"""

table_of = int(input("Enter Table of = "))
table_finalValue = int(input("Enter Table upto = "))

for x in range(1,table_finalValue):
  mulitpliedValue = table_of * x
  #print(table_of , "*" , x , "=" , mulitpliedValue)
  print(str(table_of) + "*" + str(x) + "=" + str(mulitpliedValue))



for x in range(table_finalValue , 0 , -1):
  mulitpliedValue = table_of * x
  #print(table_of , "*" , x , "=" , mulitpliedValue)
  print(str(table_of) + "*" + str(x) + "=" + str(mulitpliedValue))

"""Write a program to greet all the person names stored in a list l1 and which starts with S

l1 = ["Harry" , "Sahan" , "Sachin" , "Rahul"]
"""

l1 = ["Harry" , "Sahan" , "Sachin" , "Rahul"]
for x in range(0, len(l1)):
  if(l1[x].startswith('S')):
    print("Hello " + str(l1[x]))
  else:
    print("Bye " + str(l1[x]))

print("\n")

#method 2 simple
l1 = ["Harry" , "Sahan" , "Sachin" , "Rahul"]
for x in l1:
  if x.startswith('S'):
    print("Hello " + x)
  else:
    print("Bye " + x)

"""Multiplicatio table using while loop
<br>
f string used
"""

table_of = int(input("Enter Table of = "))
table_finalValue = int(input("Enter Table upto = "))
x = 1

while x < table_finalValue:
  mulitpliedValue = table_of * x
  #print(str(table_of) + "*" + str() + "=" + str(mulitpliedValue))
  # Using f String
  print(f"{table_of}x{x}={mulitpliedValue}")
  x=x+1

"""Check weather the number is prime or not"""

num = int(input("Enter a number = "))
prime = True

if(num%2 == 0 and num!=2):
  prime = False
  print(f"{num} is not Prime")
else:
    print(f"{num} is Prime")

"""Program to find sum of first n natural numbers"""

num = int(input("Enter n number = "))
x = 0
sum = 0
while x <= num:
  sum = sum + x
  x = x+1

print(f"Total sum : {sum}")

"""Favtorial of a number"""

num = int(input("Enter a number = "))
factorialValue = 1
factList = []

for i in range(1,num+1):
  factorialValue = factorialValue * num
  print(f"{num} * ")
  factList.append(num)
  num = num-1
print(f"Sum of factorial is : {factorialValue}")
print(f"List : {factList}")

num = int(input("Enter no of number = "))

for x in range(0,num):
  print("*" * (x + 1) )

  
for x in range(num):
  print(" " * (num-x-1) , end="-")
  print("*" * (2*x+1), end="?") 
  print(" " * (num-x-1))
 
