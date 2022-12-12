#Python Reference Guide Examples
#Page 1
#Section 6: Assignment operators

#Output headings
print("Assignment operators:")
print("---------------------\n")

input1 = 30
input2 = 15

# = simple assignment           x=y
x = 30
y = 15
x = y
print("x ", input1, "\t=\t\t\t y: ", input2, "\t\tresult x is now: ",x)

# += increment assignment       x+=y
x = 30
y = 15
x += y
print("x ", input1, "\t+=\t\t\t y: ", input2, "\t\tresult x is now: ",x)

# -= decrement assignment       x-=y
x = 30
y = 15
x -= y
print("x ", input1, "\t-=\t\t\t y: ", input2, "\t\tresult x is now: ",x)

# *= multiplication assignment  x*=y
x = 30
y = 15
x *= y
print("x ", input1, "\t*=\t\t\t y: ", input2, "\t\tresult x is now: ",x)

# %= remainder assignment       x%=y
x = 30
y = 15
x %= y
print("x ", input1, "\t%=\t\t\t y: ", input2, "\t\tresult x is now: ",x)

# /= division assignment        x/=y
x = 30
y = 15
x /= y
print("x ", input1, "\t/=\t\t\t y: ", input2, "\t\tresult x is now: ",x)

# //= floor division assignment x//=y
x = 30
y = 15
x //= y
print("x ", input1, "\t//=\t\t\t y: ", input2, "\t\tresult x is now: ",x)
