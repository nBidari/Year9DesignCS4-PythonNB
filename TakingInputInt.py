#Input
#Assignment Statement

r = int(input("What is the radius?: "))

h = int(input("What is the height?: "))

#Casting is the process of changing type
#Strings - collections of characters
#Int - integers
#Float - numbers with decimals

#Process

sa = 2 * 3.14 * r * h + 2 * 3.14 * r*r
sa = str(sa)

#Output

print("The surface area of your cylinder is " + sa + ".")