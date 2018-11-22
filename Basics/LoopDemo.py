#A lop is a a programming structure that can repeat a section of code

#There are two borad categories of loops
# Conditional Loops (while) : As long as condition is true
# Counted Loops (for) : uses counter of how many times loop is run.
#
# You can use any loop in any situaton but usually form a 
# design erspective there is a better loop in terms of coding
#
#If you know in advanece how many times a loop shoudn run
#a counter loop is probably a better choice
#
#
#
#If you dont know how many times a loop should run
#a conditional loop is probably a better choice


print("*****************************************************")

word = " "


while (len(word) < 6 or word.isalpha == False):
	#loop block
	word = input("Please input a word larger than 5 letters: ")


	if (len(word) < 6):
		print("I SAID LARGER THAN 5 LETTERS!!!")

	if (word.isalpha() == True):
		print("I SAID A REAL WORD!!!")


	#check condition at bottom of loop block
	#if true loop starts again


print(word + " is a seriously long word!")