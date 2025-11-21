#Type Conversion!!

a = 10
b = 20.5

print(type(a))
print(type(b))

sum  = a + b

print(sum)

#Type Casting

c = "100"
d = 200.56

print(type(c))
print(type(d))

sum = float(c) + d

print(sum)

print(type(sum))

e = 10
e = str(e)

print(type(e))

# #INPUTS IN PYTHON

#So whenever we take input from the user, it is always in string format.

input ("Please enter your name :")

name = input("Please enter your name :")
print("kaise ho bhai", name)

val = input("Can you please enter a value :")
print(type(val))

value = int(input("Please enter a subject no :"))
print("Your subject no is ", value)

floatt = float(input("Please enter a float value :"))
print("Your float value is ", floatt)

#An example of Inputs

name = input("Please enter your student name :")
age = int(input("Please enter your age :"))
marks = float(input("Please enter your marks :"))
Duration = int(input("Please enter your course duration in year :"))

print("Hello there student", name)
print("So your age is ", age)
print("As per your marks ", marks , "your are doing great")
print("Your course duration is ", Duration, "years")

