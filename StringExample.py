#Basics of String Manipulation

#Strings are enclosed in " " or ' '

#  0123       012345
# "Paul"     "Monkey"

# len ("Paul") = 4
# len ("Monkey") = 6

name = "Paul"

print(name)

sentence = name + "is cool!"

print(sentence)
print(sentence + "!")

#access specific letters

fLetter = name[0] #name at 0
print(fLetter)

letters1 = name[0:2]
print(letters1)

letters2a = name[2:len(name)]
print(letters2a)

letters3a = name[:2]
print(letters3a)

lname = len(name) #lenght of string
print(lname)

for i in range(len(name)):
	print(name[i])
