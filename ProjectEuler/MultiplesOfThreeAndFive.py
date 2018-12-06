answerList = []
counter = 0

def multipleOfThree(num):
	return num % 3 == 0

def multipleOfFive(num):
	return num % 5 == 0

for i in range(1000):
	if multipleOfThree(i) or multipleOfFive(i):
		counter = counter + i

print(counter)