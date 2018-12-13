binaryAlph = input("Enter binary of Alphabet ")
strAlph = input("Enter Parallel Alphabet ")

bList = binaryAlph.split()
sList = strAlph

output = ""

for i in range(len(sList)-1):
	if i % 2 != 0:
		output += "[" + bList[i] + "," + "'" + sList[i] + "'" + "],		"
	else:
		output += "[" + bList[i] + "," + "'" + sList[i] + "'" + "] \n"

print(output)