#!/usr/bin/python
#TSAlvey, 30/09/2019

#This program will take one or two base 16 hexadecimal values, show the decimal
#strings and display summations of subtraction, addition and XOR.

# initializing string 
test_string1 = input("Enter a base 16 Hexadecimal:")
test_string2 = input("Enter additional Hexadecimals, else enter 0:")

# printing original string 
print("The original string 1: " + str(test_string1)) 
print("The original string 2: " + str(test_string2))
# using int() 
# converting hexadecimal string to decimal 
res1 = int(test_string1, 16) 
res2 = int(test_string2, 16) 
# print result 
print("The decimal number of hexadecimal string 1 : " + str(res1))
print("The decimal number of hexadecimal string 1 : " + str(res2)) 

basehex = test_string1
sechex = test_string2

basehexin = int(basehex, 16)
sechexin = int(sechex, 16)



sum1 = basehexin - sechexin
sum2 = basehexin + sechexin
sum3 = basehexin ^ sechexin



print("Hexidecimal string 1 subtracted from string 2:" + hex(sum1))
print("Hexidecimal string 1 added to string 2:" + hex(sum2))
print("Hexidecimal string 1 XOR to string 2:" + hex(sum3))
