def encryptionMode(encryptionAlgorithm):
	modeInput = input("What would you like to do? ")

	return modeInput

def shiftSelect(shift):
	shiftInput = input("What is your shift? ")

	#I want it to restart from the top of this function is these conditions are made.
	#If this condition is not met, then it returns the shift.
	#I will use this in the function that is specific for each algorithm.
	if int(shiftInput) > 25 or int(shiftInput) < -25:
		print("Try Again")

	#One other question, should I use a different class for each algorithm?
	#So depending on the requested algorithm and the requested shift(if appliable)
	#Then it would run a specific class etc. (Is that the best use of the class?)




