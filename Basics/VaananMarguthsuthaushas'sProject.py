# loop can repeat a section of code.
# It can run the same code over and over or
# generate a pattern.

# Conditional loops: Go as long as a condition is true

# Counted loops: These loops use a counter to keep
#				 Track of how many times the loop has run
# If you know how many times a loop should run it's beter to use counter loop
# Else use conditional loop
import os
import webbrowser
import time
print("*******************************")
#Taking inputs
word = input("Please input a word with more than 5 letters ")
#print(word.isalpha())
while (len(word) < 6 or word.isalpha() == False):
	word = input("Please input a word with more than 5 letters ")
	if (len(word) < 6):
		os.system("say mission failed we will get them next time")

	if (word.isalpha() == False):
		print("Use one word")


print(word+" is seriously long!")
print("Sike get rick roll'd lmao")
time.sleep(2)
webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")