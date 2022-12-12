#Python Reference Guide Examples
#Page 2
#Section 15: Reading and writing files

#Output headings
print("Reading and writing files:")
print("--------------------------\n")

#Legend: x, y = any data values; s = string; n = number; L = List

# Ref:
# https://www.w3schools.com/python/python_file_open.asp

#Example 1

# f = open(<path>,‘r')
# f.read(<size>)
# f.readline(<size>)
# f.close()

#Open file in read mode
f = open("demofile.txt", "r")

#Return the 5 first characters of the file:
#print(f.read(5))

#Read one line of the file
print(f.readline())

#Close the file
f.close()

print("\n\n")



#Example 2

# f = open(<path>,’r’)
# for line in f:
#     <code>
# f.close()


#Open file in read mode
f = open("demofile.txt", "r")

#Loop through the file line by line:
for line in f:
  print(line)
f.close()



#Example 3

# f = open(<path>,'w')
# f.write(<str>)
# f.close()

#Open file in write mode, creates file if it doesn't exist
f = open("myfile",'w')

#Write a line to the file (overwrites existing content of file)
f.write("Hello there")

#Close the file
f.close()

