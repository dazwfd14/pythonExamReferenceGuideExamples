#Python Reference Guide Examples
#Page 2
#Section 16: Functions

#Output headings
print("Functions:")
print("--------\n")

#Legend: x, y = any data values; s = string; n = number; L = List

# Ref:
# https://www.w3schools.com/python/python_functions.asp


# def function(<params>):
#     <code>
# return <data> or none

#Define function first in this case with parameter x as input
def my_function(x):
  return 5 * x

#Call function many times with different arguments
print(my_function(3))
print(my_function(5))
print(my_function(9))