#Python Reference Guide Examples
#Page 2
#Section 14: Loop control statements

#Output headings
print("Loop control statements:")
print("------------------------\n")

#Legend: x, y = any data values; s = string; n = number; L = List

# Ref:
# https://www.w3schools.com/python/python_for_loops.asp

# break finishes loop execution
print("Exit the loop when x is \"banana\": ")

fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)
  if x == "banana":
    break

# continue jumps to next iteration
print("\nDo not print banana: ")

fruits = ["apple", "banana", "cherry"]

for x in fruits:
  if x == "banana":
    continue
  print(x)


# pass does nothing
print("\nif you for some reason have a for loop with no content, put in the pass statement \nto avoid getting an error.")
for x in [0, 1, 2]:
  pass
    
