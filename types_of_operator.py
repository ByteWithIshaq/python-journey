'''TYPES OF OPERATORS IN PYTHON'''

#Arithmetic Operators (+,-,*,/,%,//,**).

a = 10 
b= 5

sum = a + b
print(sum)

sum1 = a - b 
print(sum1)

sum2 = a * b
print(sum2)

sum3 = a / b                                        #Whenever we divide two numbers the result will be in float.
print(sum3)

sum4 = a % b                                        #It will give the remainder of the division. 
print(sum4)

sum5 = a // b
print(sum5)

sum6 = a ** b                                       #It will give the power of the number. like a^b
print(sum6)

#Relational / Comparison Operators (==,!=,<,>,<=,>=).

a = 50                                              #In python to check the equality of two numbers we use '=='.
b = 20                                              #Whenever we see the ! mark it means not equal to.

print(a == b) #False                                #If we want to check whether a is equal to b or not we use '=='. It will give the output in boolean. eg. True or False.
print(a != b) #True                                 #If we want to check whether a is not equal to b we use '!='. It will give the output in boolean. eg. True or False.
print(a >= b) #True                                 #if we want to compare two things in python we use ==,!=,<,>,<=,>=.
print(a > b) #True                          
print(a <= b) #False
print(a < b) #False

#Assignment Operators (=,+=,-=,*=,/=,%=,//=,**=).

num = 20
num = num + 20
num += 20                                           #we can also write num = num + 40 and num += 40 both are same.
print("num = ",num)

num1 = 20
num1 -= 20                                  
print("num1 = ",num1)

num2 = 20
num2 *= 20                                   
print("num2 = ",num2)

num3 = 20
num3 /= 20                                  
print("num3 = ",num3)

num4 = 20
num4 **= 40           
print("num4 = ",num4)

num5 = 20
num5 //= 40                                   
print("num5 = ",num5)

num6 = 20
num6 %= 40                                  
print("num6 = ",num6)

#Logical Operators (and,or,not). WORK ON BOOLEAN VALUES.
a = 100
b = 200

print(not (a < b)) #False                           #Not operator only works on one value. It will give the opposite value of the given value.

print(not True) #False
print(not False) #True

val1 = True
val2 = False

print("AND operator:", val1 and val2)               #So the and operator only give answer in True if both the values are True.
print("OR operator :", val1 or val2)                #So the or operator only give answer in True if any one of the value is True. 

print((a < b) or (a == b))
print((a < b) and (a == b))