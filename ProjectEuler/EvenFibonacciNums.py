nums = [1, 2]
value = 2
lastValue = 1
counter = 0

sumList = []

while lastValue + value < 4000000:
	nums.append(value + lastValue)

	value = value + lastValue
	lastValue = value - lastValue

for i in range(len(nums)):
	if nums[i] % 2 == 0:
		sumList.append(nums[i])

for j in range(len(sumList)):
	counter += sumList[j]

print(counter)