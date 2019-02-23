# abcdefghijklmnopqrstuvwxyz
# Exceptions: c g l r
# Closest to a: b
# Closest to e: d f
# Closest to i: h j k
# Closest to o: m n p q
# Closest to u: s t v w x y z

cnsnt =[["b"], #a
		["d","f"], #e
		["h","j","k"], #i
		["m","n","p","q"], #o
		["s","t","v","w","x","y","z"] #u
	   ]

inputStr = input("")
outputStr = ""

for i in range(len(inputStr)):
	outputStr += inputStr[i]

	if inputStr[i] in cnsnt[0]:
		outputStr += 

print(outputStr)