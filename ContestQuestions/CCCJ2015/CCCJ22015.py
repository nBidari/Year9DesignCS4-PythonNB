happy = 0
sad = 0

inputStr = input("")

for i in range(len(inputStr)-3):
	if inputStr[i:i+3] == ":-)":
		happy += 1
	elif inputStr[i:i+3] == ":-(":
		sad += 1

print(str(happy) + " " + str(sad))

if happy > sad:
	print("happy")
elif happy < sad:
	print("sad")
elif sad == 0 and happy == 0:
	print("none")
else:
	print("unsure")