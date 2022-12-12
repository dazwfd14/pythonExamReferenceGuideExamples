#Python Reference Guide Examples
#Page 2
#Section 12: Conditional statements

#Output headings
print("Conditional statements:")
print("-----------------------\n")

#Legend: x, y = any data values; s = string; n = number; L = List

# Ref: https://www.w3schools.com/python/python_conditions.asp

# if <condition> :
#     <code>
# elif <condition> :
#     <code>
# ...
# else:
#     <code>

a = 200
b = 33

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

print()

# if <value> in <list>:
#Ref: https://www.w3schools.com/python/python_lists_comprehension.asp

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)