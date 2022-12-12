#Python Reference Guide Examples
#Page 2
#Section 13: Loops

#Output headings
print("Loops:")
print("------\n")

#Legend: x, y = any data values; s = string; n = number; L = List

# Ref:
# https://www.w3schools.com/python/python_while_loops.asp
# https://www.w3schools.com/python/python_for_loops.asp

# while <condition>:
#     <code>
    
print("Print i as long as i is less than 6: ")

i = 1
while i < 6:
  print(i)
  i += 1


# for <variable> in <list>:
#     <code>

print("\nPrint each fruit in a fruit list: ")

fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)
    
# for <variable> in range(start,stop,step):
#     <code>

print("\nIncrement the sequence with 3 (default is 1): ")

for x in range(2, 30, 3):
  print(x)
