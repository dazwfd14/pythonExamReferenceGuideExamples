#Python Reference Guide Examples
#Page 1
#Section 3: Comparison operators

#Output headings
print("Comparison operators:")
print("---------------------\n")

x = 4
y = 3
result = False


# == equal
result = (x == y)
print("Is x: ", x, "\tequal to\t\t y: ", y, "\t\tresult: ",result)

# != not equal
result = (x != y)
print("Is x: ", x, "\tNot equal to\t\t y: ", y, "\t\tresult: ",result)

# > higher
result = (x > y)
print("Is x: ", x, "\tGreater than\t\t y: ", y, "\t\tresult: ",result)

# < lower
result = (x < y)
print("Is x: ", x, "\tLess than\t\t y: ", y, "\t\tresult: ",result)

# >= higher or equal
result = (x >= y)
print("Is x: ", x, "\tGreater than or equal to y: ", y, "\t\tresult: ",result)

# <= lower or equal
result = (x <= y)
print("Is x: ", x, "\tLess than or equal to\t y: ", y, "\t\tresult: ",result)