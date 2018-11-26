class Instacrypt:
	def __init__(self):

		self.finalOutput = " "

		self.action = input("Are you encoding? Y/N: ")
		self.mode = input("What encryption algorithm would you like? ")
		self.shift = int(input("What is your shift? "))

		self.inputVar = input("What is your phrase?")

		print(self.finalOutput)

		


	def encryptAscii(self): 

		for i in range(len(self.inputVar)-1):
			self.finalOutput += ord(self.inputVar) + " "

		print("test")



mainPage = Instacrypt()


