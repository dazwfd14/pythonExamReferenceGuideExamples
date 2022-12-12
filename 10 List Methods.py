#Python Reference Guide Examples
#Page 1
#Section 10: List Methods

#Output headings
print("List Methods:")
print("----------------\n")

#Legend: x, y = any data values; s = string; n = number; L = List

#populate list
list = ["Apple", "Tomato", "Orange", "Cherry","Tomato"]
print(list)

# list.append(x) appends x to the end of the list
list.append("Grape")
print(list)

# list.extend(L) appends L to the end of the list
list2 = ["Blueberry","Blackberry"]
list.extend(list2)
print(list)

# list.insert(i,x) inserts x at i position
list.insert(3,"Apple")
print(list)

# list.remove(x) removes the first list item whose value is x
list.remove("Apple")
print(list)

# list.pop(i) removes the item at position i and returns its value
list.pop(2)
print(list)

# list.index(x) returns the position of the first occurrence of x in a list
list.index("Cherry")
print(list)

# list.count(x) returns the number of times x appears in a list
list.count("Cherry")
print(list)

# list.sort() sorts items in a list
list.sort()
print(list)

# sorted(L) returns a new list with L items sorted
newList = sorted(list)
print(newList)

# list.reverse() reverses list elements
list.reverse()
print(list)

# list.copy() returns a copy of the list
copyList = list.copy()
print(copyList)

# list.clear() removes all items from the list
list.clear()
print("List contents: ",list)