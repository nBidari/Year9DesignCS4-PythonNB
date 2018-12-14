# Created by Nima Bidari December 6 2018

import tkinter as tk
import webbrowser


class Instacrypt:


	def __init__(self):

		self.outputStr = ""

		####### Language VARS ########

		self.englishTrans = ["Action", "Encode", "Decode", "Shift", "Submit","Import to Text File", "Export to Text File", "Give us feedback :)", "Our Website!"]
		self.frenchTrans  = ["Action", "Encoder", "Décoder", "Décalage", "Submitter","Importer Dans Un Fichier Texte", "Exporter Dans Un Fichier Texte", "Donnez-nous vos commentaires :)", "Notre Site Web!"]
		self.spanishTrans = ["Acción", "Codificar", "Descodificar", "El Cambio", "Enviar", "Importar Desde Archivo de Texto", "Exportar a Archivo de Texto", "Danos su opinión :)", "Nuestra Página Web!"]

		####### DESC VARS #############

		self.adList  = ["Description of Algorithsm...",
						"ASCII is the language of keyboards worldwide. It  qualitates each letter on your keyboard as 3 numbe-rs. If it is two, like 95, it would be 095. ASCII  is the hexadecimal form of the binary. (See binary for more details)",
						"Binary is a series of 1’s and 0’s 1’s represent onand 0’s represent off. This is useful in  computers as the way the processor works is to run many hund-reds of millions ons and offs every second in orderto complete a function. Binary is actually the hex-adecimal form of the ASCII as well. The most  basic form of everything  that  happens in a computer is binary.",
						"ROTI is a basic form of encryption that best rese-mbles something that may be happening  in  reality.Commonly known as the shift cipher, ROTI essentiallyshifts everything down a certain number. For examp-le, with a shift of 2, A  becomes  C. It is frequentpractice to move Z back to A, however that would me-an that the shift does not account for commas etc. -In order to keep it as realistic to how other encry-ption algorithms would work, this is the case. Thir-d-Party Encryption Algorithms have a key,  which  isassigned to the user (you). This key is much  like  the shift. When the key is used, the files will turnback to how they were originally. This happens pass-ively with all folders on a computer (i.e. admin fi-les aren’t aloud to be opened on a library computer ), however TPE’s take it a step further.",
						"Binary inversion is an interesting  one.  Althoughthe syntax looks just like binary, it is essential-ly the binary code mirrored. The same way abc wouldbecome cba. This is more  like a  code  that  wouldhave been used in WWII. A letter would be written, which seems totally normal, however in that letter there is a secret embedded. Here, if you try to de-code the binary, it would look like a corrupted fi-le, however if you invert it and then decode, then it becomes completely normal."

		]
		
		self.cdList  = ["Small description of code behind it, as well as the restrictions...",
						"ASCII Encode",
						"Binary Encode CHANGE TEXT",
						"ROTI Encode",
						"Binary Inversion Encode",
						"ASCII Decode THIS IS THE CODE",
						"Binary Decode",
						"ROTI Decode",
						"BINARY inversion decode"

		]

		######## IMPORT/EXPORT FILE SETUP ##########
		
		self.fileName = ""

		######################## ROOT ############################
	
		self.root = tk.Tk()
		self.root.title("InstaCrypt")
		self.root.configure(background = "#DADFDF")


		##################### TKINTER VARS ########################
		self.languageVar = tk.StringVar(self.root)
		self.algorithmVar = tk.StringVar(self.root)

		self.actionRadioVar = tk.IntVar(self.root)
		self.actionRadioVar.set(1)


		self.languageList = ["Language Select","English", "Espanol", "Francais"]
		self.algorithmList = ["Encryption Algorithm", "ASCII", "Binary", "ROTI", "Binary Inversion"]

		########################################################################


		############################ ACTIONS ##################################

		self.actionFrame = tk.LabelFrame(self.root, text = self.englishTrans[0])
		self.actionFrame.config(background = "#DADFDF", relief = "sunken")
		self.actionFrame.grid(row = 0, column = 0, rowspan = 2,sticky = 'W', padx = 15, pady = 5)

		self.encodeRadio = tk.Radiobutton(self.actionFrame, text = self.englishTrans[1], variable = self.actionRadioVar, value = 1)
		self.encodeRadio.config(background = "#DADFDF")
		self.encodeRadio.grid(sticky = "W")

		self.decodeRadio = tk.Radiobutton(self.actionFrame, text = self.englishTrans[2], variable = self.actionRadioVar, value = 2)
		self.decodeRadio.config(background = "#DADFDF")
		self.decodeRadio.grid(row = 1, sticky = "W")


		############## #Dropdown's (Language and Encryption Alogrithm) ############
		
		self.languageVar.set(self.languageList[0])
		self.languagedrop = tk.OptionMenu(self.root, self.languageVar, *self.languageList)
		self.languagedrop.config(background = "#DADFDF")
		self.languagedrop.grid(row = 0, column = 2, sticky = 'NSEW')

		self.algorithmVar.set(self.algorithmList[0])
		self.algorithmdrop = tk.OptionMenu(self.root, self.algorithmVar, *self.algorithmList)
		self.algorithmdrop.config(background = "#DADFDF")
		self.algorithmdrop.grid(row = 1, column = 2, sticky = 'NSEW')


		########## Input to Output (Input,Output, Shift, Submit) ###############

		self.inputEnt = tk.Text(self.root, background = "black", foreground = "lime",
									height = 10, width = 65)
		self.inputEnt.config(highlightbackground = "#074C0A")
		self.inputEnt.grid(row = 3, column = 0, columnspan = 4, sticky = 'W', padx = 5, pady = 5)

		self.inputEnt.insert(tk.INSERT, "Input goes here....")



		self.shiftFrame = tk.LabelFrame(self.root, text = self.englishTrans[3])
		self.shiftFrame.config(background = "#DADFDF", relief = "sunken")
		self.shiftFrame.grid(row = 4, column = 0, padx = 20)

		self.shiftSpin = tk.Spinbox(self.shiftFrame, from_ = -25, to = 25, width = 8)
		self.shiftSpin.config(background = "#DADFDF", highlightbackground = "#DADFDF")
		self.shiftSpin.pack()

		self.submitbtn = tk.Button(self.root, text = self.englishTrans[4], width = 25, height = 2, command = self.submitfnc)
		self.submitbtn.config(background = "#DADFDF", relief = "sunken", highlightbackground = "#232423")
		self.submitbtn.grid(row = 4, column = 1, columnspan = 2, sticky = 'SW', pady = 5)

		self.outputEnt = tk.Text(self.root, background = "black", foreground = "lime",
									height = 10, width = 65)
		self.outputEnt.config(highlightbackground = "#074C0A")
		self.outputEnt.grid(row = 5, column = 0, columnspan = 4, rowspan = 7, sticky = 'NESW', padx = 5, pady = 5)



		self.outputEnt.insert(tk.INSERT, "Output will go here...")


		########################## Descriptions ####################################

		self.algoDesc = tk.Text(self.root, background = "gray", foreground = "white",
										height = 5, width = 50)
		self.algoDesc.config(highlightbackground = "#232423")
		self.algoDesc.grid(row = 0, column = 6, rowspan = 3)

		self.codeDesc = tk.Text(self.root, background = "gray", foreground = "white",
										height = 10, width = 50)
		self.codeDesc.config(highlightbackground = "#232423")
		self.codeDesc.grid(row = 3, column = 6)


		self.algoDesc.insert(tk.INSERT, self.adList[0])
		self.codeDesc.insert(tk.INSERT, self.cdList[0])

		self.algoDesc.config(state = "disabled")
		self.codeDesc.config(state = "disabled")

		###################### Import Export Buttons ##############################

		self.importbtn = tk.Button(self.root, text = self.englishTrans[5], 
											height = 2, width = 40, command = self.importfnc)
		self.importbtn.config(highlightbackground = "#232423")
		self.importbtn.grid(row = 4, column = 6, padx = 12)

		self.exportbtn = tk.Button(self.root, text = self.englishTrans[6], 
											height = 2, width = 40, command = self.exportfnc)
		self.exportbtn.config(highlightbackground = "#232423")
		self.exportbtn.grid(row = 5, column = 6)

		self.fileEntry = tk.Text(self.root, height = 1, width = 40)
		self.fileEntry.config(highlightbackground = "#232423")
		self.fileEntry.grid(row = 6, column = 6, padx = 12, pady = 6)

		self.fileEntry.insert(tk.INSERT, "Enter your file name here...")


		######################## WEBSITE REDIRECTS #################################

		self.feedbackSite = tk.Button(self.root, text = self.englishTrans[7], command = self.feedbackWebOpener, height = 2)
		self.feedbackSite.config(highlightbackground = "#232423")
		self.feedbackSite.grid(row = 7, column = 6, padx = 12, pady = 6, sticky = "EW")

		self.webSite = tk.Button(self.root, text = self.englishTrans[8], command = self.websiteWebOpener, height = 2)
		self.webSite.config(highlightbackground = "#232423")
		self.webSite.grid(row = 8, column = 6, padx = 12, pady = 6, sticky = "EW")

		############################# LOGO #########################################
		
		self.logo = tk.PhotoImage(file = "InstaCryptLogo.png")
		self.logoImage = tk.Label(image = self.logo)
		self.logoImage.config(background = "#232423")
		self.logoImage.grid(row = 9, column = 6, sticky = "N", padx = 12)


		self.root.mainloop()

############################ END OF  ROOT ##############################################

	###################### IMPORT/EXPORT #####################

	def exportfnc(self):
		self.fileName = self.fileEntry.get("1.0", tk.END)
		print(self.fileName)

		self.file = open(self.fileName + ".txt", "a") #This way the person doesn't need to know to write down a suffix.
													  #Maybe in the future the file type can be specified

		inputStr =  self.inputEnt.get("1.0", tk.END)
		outputStr = self.outputEnt.get("1.0", tk.END)

		self.file.write(outputStr + "\n") 

	def importfnc(self):
		self.fileName = self.fileEntry.get("1.0", tk.END)

		self.file = open(self.fileName + ".txt", "r") #This way the person doesn't need to know to write down a suffix.
													  #Maybe in the future the file type can be specified

		if self.file.mode == "r":
			self.contents = self.file.read()


		self.inputEnt.insert(tk.INSERT, self.contents)

	##########################################################







	########################### ENCRYPTION ALGORITMS ###################################
	def asciiEncode(self):

		inputStr = self.inputEnt.get("1.0", tk.END)
		
		for i in range(len(inputStr)):

			if len(str(ord(inputStr[i]))) <= 2:
				self.outputStr += "0"
				self.outputStr += str(ord(inputStr[i]))
				self.outputStr += " "
			else:
				self.outputStr += str(ord(inputStr[i]))
				self.outputStr += " "
		

		self.outputEnt.delete("1.0", tk.END)
		self.outputEnt.update()

		self.outputEnt.insert(tk.INSERT, self.outputStr[0:len(self.outputStr)-4]) #This is due to a bug, no fix found, so
																				  #instead just removed it from the output.



	def binaryEncode(self):

		inputStr = self.inputEnt.get("1.0", tk.END)

		str = ' '.join(format(ord(x), 'b') for x in inputStr) #Simple .format() function in cooperation with .join()
															  #This way it can be done in one line, not really 
															  #necessary, just more efficient

		self.outputEnt.delete("1.0", tk.END)
		self.outputEnt.update()

		self.outputEnt.insert(tk.INSERT, str[0:len(str) - 5]) #Bug fix


	def rotiEncode(self):
		inputStr = self.inputEnt.get("1.0", tk.END)
		shift = int(self.shiftSpin.get())


		for x in range(len(inputStr)-1):
			self.outputStr += chr(int(ord(inputStr[x]) + shift)) #Simple two line solution in cooperation with ASCII
																 #This means that I don't have to use a library.



		self.outputEnt.delete("1.0", tk.END)
		self.outputEnt.update()

		self.outputEnt.insert(tk.INSERT, self.outputStr)





	def binaryInversionEncode(self):

		inputStr = self.inputEnt.get("1.0", tk.END)

		str = ' '.join(format(ord(x), 'b') for x in inputStr) #
		self.outputStr = str[::-1] 							  #


		self.outputEnt.delete("1.0", tk.END)
		self.outputEnt.update()

		self.outputEnt.insert(tk.INSERT, self.outputStr[5:len(self.outputStr)])





	######################## DECRYPTION ALGORITHMS ###################################


	def asciiDecode(self):

		inputStr = self.inputEnt.get("1.0", tk.END)

		inputList = []

		#This is making a list of all of the individual ascii numbers

		for i in range(len(inputStr)-1):

			inputList = inputStr.split()


		#This is turning those into characters and putting them into words without spaces 
		#	(common practice to not include spaces unless specified by the encryption)

		for x in range(len(inputList)):
			self.outputStr += chr(int(inputList[x]))


		self.outputEnt.delete("1.0", tk.END)
		self.outputEnt.update()

		self.outputEnt.insert(tk.INSERT, self.outputStr)




	def binaryDecode(self):
		
		inputStr = self.inputEnt.get("1.0", tk.END)

		inputList = inputStr.split()

		for i in range(len(inputList)):
			inputList[i] = int(inputList[i])

		self.decode(inputList)


		self.outputEnt.delete("1.0", tk.END)
		self.outputEnt.update()

		self.outputEnt.insert(tk.INSERT, self.outputStr)


	def rotiDecode(self):
		inputStr = self.inputEnt.get("1.0", tk.END)
		shift = int(self.shiftSpin.get())

		for x in range(len(inputStr)):
			self.outputStr += chr(int(ord(inputStr[x]) - shift))



		self.outputEnt.delete("1.0", tk.END)
		self.outputEnt.update()

		self.outputEnt.insert(tk.INSERT, self.outputStr[0:len(self.outputStr)-2])


	def binaryInversionDecode(self):
		inputStr = self.inputEnt.get("1.0", tk.END)
		inputStr = inputStr[::-1]

		inputList = inputStr.split()

		for i in range(len(inputList)):
			inputList[i] = int(inputList[i])

		self.decode(inputList)

		self.outputEnt.delete("1.0", tk.END)
		self.outputEnt.update()

		self.outputEnt.insert(tk.INSERT, self.outputStr)


		


	############ WEB BROWSER ############

	def feedbackWebOpener(self):
		webbrowser.open("https://sites.google.com/ucc.on.ca/year9designcoding-nbidari/unit-1/evaluating/feedback?authuser=1")
	def websiteWebOpener(self):
		webbrowser.open("https://sites.google.com/ucc.on.ca/year9designcoding-nbidari/home?authuser=1")


	################################ BINARY LIBRARY ##################################
	def decode(self,message):

		dList = [

				[1100001, "a"],		[1100010, "b"],
				[1100011, "c"],		[1100100, "d"],
				[1100101, "e"],		[1100110, "f"],
				[1100111, "g"],		[1101000, "h"],
				[1101001, "i"],		[1101010, "j"],
				[1101011, "k"],		[1101100, "l"],
				[1101101, "m"],		[1101110, "n"],
				[1101111, "o"],		[1110000, "p"],
				[1110001, "q"],		[1110010, "r"],
				[1110011, "s"],		[1110100, "t"],
				[1110101, "u"],		[1110110, "v"],
				[1110111, "w"],		[1111000, "x"],
				[1111001, "y"],		[1111010, "z"],
				[1000001, 'A'], 	[1000010, 'B'], 
				[1000011, 'C'], 	[1000100, 'D'], 
				[1000101, 'E'],		[1000110, 'F'], 
				[1000111, 'G'], 	[1001000, 'H'], 
				[1001001, 'I'], 	[1001010, 'J'], 
				[1001011, 'K'], 	[1001100, 'L'], 
				[1001101, 'M'], 	[1001110, 'N'], 
				[1001111, 'O'], 	[1010000, 'P'], 
				[1010001, 'Q'], 	[1010010, 'R'], 
				[1010011, 'S'], 	[1010100, 'T'], 
				[1010101, 'U'], 	[1010110, 'V'], 
				[1010111, 'W'], 	[1011000, 'X'], 
				[1011001, 'Y'], 	[1011010, 'Z'],
				[100001,  '!'],		[1000000, '@'],
				[100011,  '#'],		[100100,  '$'],
				[100101,  '%'],		[1011110, '^'], 
				[100110,  '&'],		[101010,  '*'], 
				[101000,  '('],		[101001,  ')'], 
				[1011111, '_'],		[101011,  '+'], 
				[1100000, '`'],		[110001,  '1'], 
				[110010,  '2'],		[110011,  '3'], 
				[110100,  '4'],		[110101,  '5'], 
				[110110,  '6'],		[110111,  '7'], 
				[111000,  '8'],		[111001,  '9'], 
				[110000,  '0'],		[101101,  '-'], 
				[111101,  '='],		[111011,  ';'], 
				[111100,  '<'], 	[1111110, '~'],
				[111110,  '>'],		[111111,  '?'],
				[100000,  ' ']
			]

		self.outputStr = ""

		for i in range(0,len(message),1):
			for j in range(0, len(dList), 1): #loops through dlist
				if dList[j][0] == message[i]:
					self.outputStr = self.outputStr + dList[j][1]



	########################## SUBMIT FUNCTION #######################################

	def submitfnc(self):

		adOutput = ""
		cdOutput = ""

		self.outputEnt.delete("1.0", tk.END)

		try:


			self.outputEnt.delete("1.0", tk.END)

			if self.actionRadioVar.get() == 1:

				if self.algorithmVar.get() == "ASCII":
					self.asciiEncode()

					adOutput = self.adList[1]
					cdOutput = self.cdList[1]

				elif self.algorithmVar.get() == "Binary":
					self.binaryEncode()

					adOutput = self.adList[2]
					cdOutput = self.cdList[2]

				elif self.algorithmVar.get() == "ROTI":
					self.rotiEncode()

					adOutput = self.adList[3]
					cdOutput = self.cdList[3]

				elif self.algorithmVar.get() == "Binary Inversion":
					self.binaryInversionEncode()

					adOutput = self.adList[4]
					cdOutput = self.cdList[4]
			else:

				if self.algorithmVar.get() == "ASCII":
					self.asciiDecode()

					adOutput = self.adList[1]
					cdOutput = self.cdList[5]

				elif self.algorithmVar.get() == "Binary":
					self.binaryDecode()

					adOutput = self.adList[2]
					cdOutput = self.cdList[6]

				elif self.algorithmVar.get() == "ROTI":
					self.rotiDecode()

					adOutput = self.adList[3]
					cdOutput = self.cdList[7]

				elif self.algorithmVar.get() == "Binary Inversion":
					self.binaryInversionDecode()

					adOutput = self.adList[4]
					cdOutput = self.cdList[8]


		except ValueError: #This is for when there are 
						   #non-alpha chars in the input (Mandarin, Arabic,
						   #letters in ASCII or Binary decoding etc.)

			adOutput = "INVALID INPUT"
			cdOutput = "INVALID INPUT"


			self.outputEnt.delete("1.0", tk.END)
			self.outputEnt.update()

			self.outputEnt.insert(tk.INSERT, "INVALID")


		###### Language Change #####

		if self.languageVar.get() == "English":
			self.actionFrame.config(text = self.englishTrans[0])
			self.encodeRadio.config(text = self.englishTrans[1])
			self.decodeRadio.config(text = self.englishTrans[2])
			self.shiftFrame.config(text  = self.englishTrans[3])
			self.submitbtn.config(text   = self.englishTrans[4])
			self.importbtn.config(text   = self.englishTrans[5])
			self.exportbtn.config(text   = self.englishTrans[6])
			self.feedbackSite.config(text= self.englishTrans[7])
			self.webSite.config(text     = self.englishTrans[8])

		elif self.languageVar.get() == "Francais":
			self.actionFrame.config(text = self.frenchTrans[0])
			self.encodeRadio.config(text = self.frenchTrans[1])
			self.decodeRadio.config(text = self.frenchTrans[2])
			self.shiftFrame.config(text  = self.frenchTrans[3])
			self.submitbtn.config(text   = self.frenchTrans[4])
			self.importbtn.config(text   = self.frenchTrans[5])
			self.exportbtn.config(text   = self.frenchTrans[6])
			self.feedbackSite.config(text= self.frenchTrans[7])
			self.webSite.config(text     = self.frenchTrans[8])

		elif self.languageVar.get() == "Espanol":
			self.actionFrame.config(text = self.spanishTrans[0])
			self.encodeRadio.config(text = self.spanishTrans[1])
			self.decodeRadio.config(text = self.spanishTrans[2])
			self.shiftFrame.config(text  = self.spanishTrans[3])
			self.submitbtn.config(text   = self.spanishTrans[4])
			self.importbtn.config(text   = self.spanishTrans[5])
			self.exportbtn.config(text   = self.spanishTrans[6])
			self.feedbackSite.config(text= self.spanishTrans[7])
			self.webSite.config(text     = self.spanishTrans[8])

			#Unfortunately could not find a better way to do this.



		#Just a Reset
		self.outputStr = ""


		##### DESC INSERTS #####
		self.algoDesc.config(state = "normal")
		self.codeDesc.config(state = "normal")

		self.algoDesc.delete("1.0", tk.END)
		self.algoDesc.update()

		self.algoDesc.insert(tk.INSERT, adOutput)

		self.codeDesc.delete("1.0", tk.END)
		self.codeDesc.update()

		self.codeDesc.insert(tk.INSERT, cdOutput)

		self.algoDesc.config(state = "disabled")
		self.codeDesc.config(state = "disabled")





mainPage = Instacrypt()










