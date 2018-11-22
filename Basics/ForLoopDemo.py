print("********************************************")
print("Counted Loop: For")


#When we think of a for loop
# Count: The variable that holds the current count
# Check: The check that is doneeach time the loop runs
# Change: The change applied to the coutn each time the loop runs


for i in range(0,400000,1):
	print(i)
	if( i % 2 == 0):
		print(str(i) + " is even.")
	else:
		print(str(i) + " is odd.")
