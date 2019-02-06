import string
import random

fName = open("nameList.txt", "r")
emailList = open("emailList.txt", "a")
passList = open("passList.txt", "a")


fContents = fName.read()
fContents = fContents.split("\n")

outputStr = ""
outputPass = []

for y in range(len(fContents)-1):
	fContents[y] = str(fContents[y])

for i in range(len(fContents)-1):
	for x in range(len(fContents)-1):
		outputStr += fContents[i].lower() + "." + fContents[x].lower() + random.choice()"\n"

emailList.write(outputStr)



for j in range(1,1000001):
	
	

passList.write(outputPass)

