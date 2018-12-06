import tkinter as tk

class Instacrypt:


	def __init__(self):

		####### Language VARS ########

		self.englishTrans = ["Action", "Encode", "Decode", "Shift", "Submit","Import to Text File", "Export to Text File"]
		self.frenchTrans  = ["Action", "Encoder", "Décoder", "Décalage", "Submitter","Importer Dans Un Fichier Texte", "Exporter Dans Un Fichier Texte"]
		self.spanishTrans = ["Acción", "Codificar", "Descodificar", "El Cambio", "Enviar", "Importar Desde Archivo de Texto", "Exportar a Archivo de Texto"]

		######## IMPORT/EXPORT FILE SETUP ##########
		self.fileName = ""

		######################## ROOT ############################
	
		self.root = tk.Tk()
		self.root.title("InstaCrypt")
		self.root.configure(background = "#DADFDF")

		###########################################################


		##################### TKINTER VARS ########################
		self.languageVar = tk.StringVar(self.root)
		self.algorithmVar = tk.StringVar(self.root)

		self.actionRadioVar = tk.IntVar(self.root)
		self.actionRadioVar.set(1)


		self.languageList = ["Language Select","English", "Espanol","Farsi", "Francais"]
		self.algorithmList = ["Encryption Algorithm", "ASCII", "Binary", "ROTI",
										 "ASCII-Binary", "Binary Inversion"]

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

		#######################################################################


		############## #Dropdown's (Language and Encryption Alogrithm) ############
		
		self.languageVar.set(self.languageList[0])
		self.languagedrop = tk.OptionMenu(self.root, self.languageVar, *self.languageList)
		self.languagedrop.config(background = "#DADFDF")
		self.languagedrop.grid(row = 0, column = 2, sticky = 'NSEW')

		self.algorithmVar.set(self.algorithmList[0])
		self.algorithmdrop = tk.OptionMenu(self.root, self.algorithmVar, *self.algorithmList)
		self.algorithmdrop.config(background = "#DADFDF")
		self.algorithmdrop.grid(row = 1, column = 2, sticky = 'NSEW')

		#######################################################################


		########## Input to Output (Input,Output, Shift, Submit) ###############

		self.inputEnt = tk.Text(self.root, background = "black", foreground = "lime",
									height = 10, width = 65)
		self.inputEnt.config(highlightbackground = "#074C0A")
		self.inputEnt.grid(row = 3, column = 0, columnspan = 4, sticky = 'W', padx = 5, pady = 5)


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
		self.outputEnt.config(state = "disabled", highlightbackground = "#074C0A")
		self.outputEnt.grid(row = 5, column = 0, columnspan = 4, rowspan = 3, sticky = 'W', padx = 5, pady = 5)

		#########################################################################


		########################## Descriptions ####################################

		self.algoDesc = tk.Text(self.root, background = "gray", foreground = "white",
										height = 5, width = 50)
		self.algoDesc.config(state = "disabled", highlightbackground = "#232423")
		self.algoDesc.grid(row = 0, column = 6, rowspan = 3)

		self.codeDesc = tk.Text(self.root, background = "gray", foreground = "white",
										height = 10, width = 50)
		self.codeDesc.config(state = "disabled", highlightbackground = "#232423")
		self.codeDesc.grid(row = 3, column = 6)

		###########################################################################


		###################### Import Export Buttons ##############################

		self.importbtn = tk.Button(self.root, text = self.englishTrans[5], 
											height = 2, width = 40, command = self.importfnc)
		self.importbtn.config(highlightbackground = "#232423")
		self.importbtn.grid(row = 4, column = 6, padx = 12)

		self.exportbtn = tk.Button(self.root, text = self.englishTrans[6], 
											height = 2, width = 40, command = self.exportfnc)
		self.exportbtn.config(highlightbackground = "#232423")
		self.exportbtn.grid(row = 5, column = 6)

		self.fileEntry = tk.Entry(self.root)
		self.fileEntry.config(highlightbackground = "#232423")
		self.fileEntry.grid(row = 6, column = 6, padx = 12, pady = 6)

		############################################################################


		############################# LOGO #########################################
		
		self.logo = tk.PhotoImage(file = "InstaCryptLogo.png")
		self.logoImage = tk.Label(image = self.logo)
		self.logoImage.config(background = "#232423")
		self.logoImage.grid(row = 7, column = 6, sticky = "NW", padx = 12)
		
		##############################################################################


		self.outputStr = ""


		self.root.mainloop()

############################ END OF  ROOT ##############################################

	###################### IMPORT/EXPORT #####################

	def exportfnc(self):
		self.fileName = self.fileEntry.get()

		self.file = open(self.fileName + ".txt", "a")

		inputStr =  self.inputEnt.get("1.0", tk.END)
		outputStr = self.outputEnt.get("1.0", tk.END)

		self.file.write(inputStr + "\n" + outputStr + "\n")

	def importfnc(self):
		self.fileName = self.fileEntry.get()

		self.file = open(self.fileName + ".txt", "r")

		if self.file.mode == "r":
			self.contents = self.file.read()


		self.inputEnt.insert(tk.INSERT, self.contents)

	##########################################################



	########################### ENCRYPTION ALGORITMS ###################################
	def asciiEncode(self):

		inputStr = self.inputEnt.get("1.0", tk.END)
		
		for i in range(len(inputStr)):
			
			print(i)

			if len(str(ord(inputStr[i]))) <= 2:
				self.outputStr += "0"
				self.outputStr += str(ord(inputStr[i]))
				self.outputStr += " "
			else:
				self.outputStr += str(ord(inputStr[i]))
				self.outputStr += " "
		
		self.outputEnt.config(state = 'normal')

		self.outputEnt.delete("1.0", tk.END)
		self.outputEnt.update()

		self.outputEnt.insert(tk.INSERT, self.outputStr[0:len(self.outputStr)-3])
		self.outputEnt.config(state = 'disabled')

		self.outputStr = ""

		############################

	def binaryEncode(self):

		inputStr = self.inputEnt.get("1.0", tk.END)

		self.outputStr.join(format(ord(x), 'b') for x in inputStr)

		print(self.outputStr)




	def rotiEncode(self):
		inputStr = self.inputEnt.get("1.0", tk.END)
		shift = int(self.shiftSpin.get())


		for x in range(len(inputStr)-1):
			self.outputStr += chr(int(ord(inputStr[x]) + shift))


		self.outputEnt.config(state = 'normal')

		self.outputEnt.delete("1.0", tk.END)
		self.outputEnt.update()

		self.outputEnt.insert(tk.INSERT, self.outputStr)

		self.outputEnt.config(state = 'disabled')

		self.outputStr = ""


	def asciiBinaryEncode(self):
		print("ASCII-Binary")

	def binaryInversionEncode(self):
		print("Binary Inversion")

	#################################################################################



	######################## DECRYPTION ALGORITHMS ###################################


	def asciiDecode(self):

		inputStr = self.inputEnt.get("1.0", tk.END)

		inputList = []

		#This is making a list of all of the individual ascii numbers

		for i in range(len(inputStr)-1):

			if i != 0:

				if i != len(inputStr) - 6:
					if inputStr[i] == " " and inputStr[i+5] == " ":

						print("YEET")
						inputList.append(inputStr[i+1:i+4])
						print("test")
				
					else:
						print("next" + str(i))
				else:
					inputList.append(inputStr[i+1:i+4])

			else:
				inputList.append(inputStr[i:i+3])

		print(inputList)


		#This is turning those into characters and putting them into words without spaces 
		#	(common practice to not include spaces unless specified by the encryption)

		for x in range(len(inputList)):
			self.outputStr += chr(int(inputList[x]))
			print("test 2")

		self.outputEnt.config(state = 'normal')

		self.outputEnt.delete("1.0", tk.END)
		self.outputEnt.update()

		self.outputEnt.insert(tk.INSERT, self.outputStr)
		self.outputEnt.config(state = 'disabled')

		self.outputStr = ""

	def binaryDecode(self):
		print("Binary Decode")

	def rotiDecode(self):
		inputStr = self.inputEnt.get("1.0", tk.END)
		shift = int(self.shiftSpin.get())

		for x in range(len(inputStr)-1):
			self.outputStr += chr(int(ord(inputStr[x]) - shift))



		self.outputEnt.config(state = 'normal')

		self.outputEnt.delete("1.0", tk.END)
		self.outputEnt.update()

		self.outputEnt.insert(tk.INSERT, self.outputStr)

		self.outputEnt.config(state = 'disabled')

		self.outputStr = ""


	def asciiBinaryDecode(self):
		print("Ascii-Binary Decode")

	def binaryInversionDecode(self):
		print("binary inversion decode")

	##################################################################################


	########################## SUBMIT FUNCTION #######################################

	def submitfnc(self):

		if self.actionRadioVar.get() == 1:

			if self.algorithmVar.get() == "ASCII":
				self.asciiEncode()

			elif self.algorithmVar.get() == "Binary":
				self.binaryEncode()

			elif self.algorithmVar.get() == "ROTI":
				self.rotiEncode()

			elif self.algorithmVar.get() == "ASCII-Binary":
				self.asciiBinaryEncode()

			elif self.algorithmVar.get() == "Binary Inversion":
				self.binaryInversionEncode()
		else:

			if self.algorithmVar.get() == "ASCII":
				self.asciiDecode()

			elif self.algorithmVar.get() == "Binary":
				self.binaryDecode()

			elif self.algorithmVar.get() == "ROTI":
				self.rotiDecode()

			elif self.algorithmVar.get() == "ASCII-Binary":
				self.asciiBinaryDecode()

			elif self.algorithmVar.get() == "Binary Inversion":
				self.binaryInversionDecode()


		###### Language Change #####

		if self.languageVar.get() == "English":
			self.actionFrame.config(text = self.englishTrans[0])
			self.encodeRadio.config(text = self.englishTrans[1])
			self.decodeRadio.config(text = self.englishTrans[2])
			self.shiftFrame.config(text  = self.englishTrans[3])
			self.submitbtn.config(text   = self.englishTrans[4])
			self.importbtn.config(text   = self.englishTrans[5])
			self.exportbtn.config(text   = self.englishTrans[6])

		elif self.languageVar.get() == "Francais":
			self.actionFrame.config(text = self.frenchTrans[0])
			self.encodeRadio.config(text = self.frenchTrans[1])
			self.decodeRadio.config(text = self.frenchTrans[2])
			self.shiftFrame.config(text  = self.frenchTrans[3])
			self.submitbtn.config(text   = self.frenchTrans[4])
			self.importbtn.config(text   = self.frenchTrans[5])
			self.exportbtn.config(text   = self.frenchTrans[6])

		elif self.languageVar.get() == "Espanol":
			self.actionFrame.config(text = self.spanishTrans[0])
			self.encodeRadio.config(text = self.spanishTrans[1])
			self.decodeRadio.config(text = self.spanishTrans[2])
			self.shiftFrame.config(text  = self.spanishTrans[3])
			self.submitbtn.config(text   = self.spanishTrans[4])
			self.importbtn.config(text   = self.spanishTrans[5])
			self.exportbtn.config(text   = self.spanishTrans[6])


		############################

		
		self.outputStr = ""


		# print(self.shiftSpin.get())

	

	#############################################################################






mainPage = Instacrypt()









