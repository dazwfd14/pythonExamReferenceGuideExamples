#Python Reference Guide Examples
#Page 1
#Section 8: String Methods

#Output headings
print("String Methods:")
print("----------------\n")

#initial string to process
str = "Hello World"

# string.upper() returns uppercase string
print("Uppercase string: ",str.upper())

# string.lower() returns lowercase string
print("Lowercase string: ",str.lower())

# string.count(x) counts how many times x appears
print("Count character 'o' in string: ",str.count('o'))

# string.find(x) position of the first occurrence of x
print("Find position of character 'o' in string: ",str.find('o'))

# string.replace(x,y) replaces x with y
print("Replace character 'o' in string with 'a': ",str.replace('o','a'))

# string.islower() returns True if all characters are lowercase
print("All characters lower case: ",str.islower())

# string.isupper() returns True if all characters are uppercase
print("All characters upper case: ",str.isupper())

# string.isalnum() returns True if all characters are alphanumeric
print("All alphanumeric: ",str.isalnum())

# string.isalpha() returns True if all characters are alphabetic
print("All alphabetic characters: ",str.isalpha())

# string.isdigit() returns True if all characters are digits
print("All Digti characters: ",str.isdigit())

# string.index(s) returns index of substring s in string
print("Return index of substring \"ll\": ",str.index("ll"))

# string.strip(x) returns a string with leading and trailing characters removed
str = "     Happy days    "
print("Return string with leading and trailing characters removed: ", str.strip())
      