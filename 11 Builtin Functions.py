#Python Reference Guide Examples
#Page 2
#Section 11: Built-in functions

#Output headings
print("Built-in functions:")
print("-------------------\n")

#Legend: x, y = any data values; s = string; n = number; L = List

#More examples:
#https://www.w3schools.com/python/python_ref_functions.asp


# print(x, sep='y') prints x objects separated by y
print("Hello", "how are you?", sep="---")


# input(s) prints s and waits for an input that will be returned
age = int(input("Please enter your age?: "))
print("Your age is: ",age)


# len(x) returns the length of x (s or L)
myStr = "Hello"
myList = ["Apple","Orange"]
print("\nLength of String: ",len(myStr))
print("\nLength of List: ",len(myList))


# min(L) returns the minimum value in L
myList = [1,2,3,4,5,6,0,7,8,9,10]
print("\nMin value in list: ",min(myList))

# max(L) returns the maximum value in L
myList = [1,2,3,4,5,6,0,7,8,9,10]
print("\nMax value in list: ",max(myList))

# sum(L) returns the sum of the values in L
myList = [1,2,3,4,5,6,0,7,8,9,10]
print("\nSum values in list: ",sum(myList))


# range(n1,n2,n) returns a sequence of numbers from n1 to n2 in steps of n
x = range(3, 20, 2)
print("\nRange 3 to 19 inclusive in Steps of 2: ")
for n in x:
  print(n)


# abs(n) returns the absolute value of n
num = -100.20
print("\nAbsolute value of ",num, " is ",abs(num))   ## TO DO


# round(n1,n) returns the n1 number rounded to n digits
num = 20.5245
print("\n20.5245 Rounded to 2 Decimal Places: ",round(num,2))


# type(x) returns the type of x (string,float, list ...)
myStr = "Hello"
decimal = 10.20
myList = [1,2,3,4,5]
print(type(myStr))
print(type(decimal))
print(type(myList))


# str(x) converts x to a string
pi = 3.14
##text = 'The value of pi is ' + pi      ## NO, does not work
text = "\nThe value of pi is "  + str(pi)  ## yes
print(text)


# list(x) converts x to a list
myList = list(('apple', 'banana', 'cherry'))

print("\nList: ",myList)


# int(x) converts x to an integer
str = 20
num = int(str)
print("\nString \"20\" to int: ",num)


# float(x) converts x to a float
wholeNum = 100
decimal = float(wholeNum)
print("\nInteger \"100\" to float: ",decimal)


# bool(x) converts x to a Boolean value
x = bool(1)
print(x)

# pow(n1,n2) returns n1 to the power of n2
result = pow(2,4) # 2 to the power of 4
print("\n2 to the power of 4: ",result)

# chr(x) returns the string value of a Unicode code
print("\nString value of unicode 90: ",chr(90))


# ord(x) returns the Unicode code of a single-character string
print("\nUnicode value of z: ",ord('z'))


# map(function, L) applies function to values in L   ##TO DO
# Example 1: Python program to demonstrate working of map.

# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Example 2: Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

