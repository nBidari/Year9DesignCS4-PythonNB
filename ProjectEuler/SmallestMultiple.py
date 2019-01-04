num = 1
foundNum = False
counter = 0

while foundNum == False:
	for i in range(1,21):
		if num % i  == 0:
			counter += 1

	if counter == 20:
		foundNum = True
	
	counter = 0
	num += 1

print(num)