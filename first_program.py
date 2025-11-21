# day_01/first_program.py
# Day 1 — Basic Python examples: prints, variables, types, and simple arithmetic
# Author: Ishaq Shaikh (ByteWithIshaq)


print("My name is Ishaq shaikh")                    #when we use "," in the print function it will add space between the two strings but it will continue in the same line.
print(23)                                           #In Python we can do mathematics operations in the print function.
print(23+10)                                        #Python is a case sensitive language.
name = "Ishaq Shaikh"                               #We can store the string in the variable and print it. #variable = value        
age = 18                                            #So in Python if we use "=" that means the value in the right stored in the left.                  #Value in the variable can be changed.  #Variable mean memory location. #Variable is a name given to a meomory location.
price = 20.99                                       #String means text that we want to display as it is.
age2 = age                                          #So in python we can store the variable in the other variable.

print("My name is :",name)
print("My age is :",age2)                           #The variable should be simple,short and meaningful.
print("The price is :",price)                       #So whenever we want to use the value of the variable we can use the variable name.
print(age2)                                         #So we can print the value of the variable as many times as we want.

print(type(name))
print(type(age2))
print(type(price))                                  #So we can check the type of the variable by using the type function.   #Python automatically detects the type of the variable.

age_of_me_after_3years = 21                             #so this is the first one of the primary data types in python is Intergers. eg: 29,-20,0. it comes print as type int.
print("My age after 3 years will be :",age_of_me_after_3years)

print("ISHAQ SHAIKH")                               #so this is string the "ISHAQ SHAIKH" is a string. the data we write in "" is print as it is and it called as string.

name1 = 'NAWAZ SHAIKH'                              #checking the difference between the single quotes,double quotes and triple quotes.  
name2 = "NAWAZ SHAIKH"
name3 = '''NAWAZ SHAIKH'''                                                #',"",''' '''.

print(name1)
print(name2)
print(name3)

price1 = 20.33                                       #float data comes with decimal values. TO COMMENT ISTANTLY USE CTRL+/ AND TO COMMENT MULTIPLE LINES USE ''' '''.

age3 = 25
old = False                                          #So a operator is a symbol that performs an operation on opearands.
a = None                                             #none is used to represent the absence of the value. eg: None.

print(type(old))                                     #The opearation perform on values are called as operands. eg: a+b a,b are the operands.
print(type(a))                                       #Boolean data type is used to represent the truth values. eg: True,False.

                                                     #operators are there to perform the operations just like in mathematics + do the addition. 
a = 150                                              #In mathematics a+b a is the operand and + is the operator. #operator has to do the operation like + do the addition.
b = 50
total = a+b

print(total)
print(type(total))
