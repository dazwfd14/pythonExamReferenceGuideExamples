#Python Reference Guide Examples
#Page 1
#Section 9: List Operations

#Output headings
print("List Operations:")
print("----------------\n")

#list = [] defines an empty list
list = []

#populate list
list = ["Apple", "Orange", "Cherry","Tomato"]

# list[i] = x stores x with index i
print(list) # original list
list[2] = "Grape"
print(list) # updated list

# list[i] retrieves the item with index i
print(list[0])

# list[-i] retrieves last i item from list
print(list[-1])

# list[i:j] retrieves items in the range i to j
print(list[1:3])

# list[i:] retrieves items from i to the end
print(list[2:])

#del list[i] removes the item with index i
del list[0]
print(list)

