import tkinter as tk

class Instacrypt:


	def __init__(self):

		#Variables for Data:








		self.root = tk.Tk()
		self.root.title("InstaCrypt")
		self.root.configure(background = "#DADFDF")

		self.languageList = ["Language Select","English", "Espanol","Farsi", "Francais"]
		self.algorithmList = ["Encryption Algorithm", "ASCII", "Binary", "ROTI",
										 "ASCII-Binary", "Binary Inversion"]

		self.languageVar = tk.StringVar(self.root)
		self.algorithmVar = tk.StringVar(self.root)

		self.actionRadioVar = tk.IntVar(self.root)

		#Action's

		#Initializing

		self.actionRadioVar.set(1)

		####

		self.actionFrame = tk.LabelFrame(self.root, text = "Action")
		self.actionFrame.config(background = "#DADFDF", relief = "sunken")
		self.actionFrame.grid(row = 0, column = 0, rowspan = 2,sticky = 'W', padx = 15, pady = 5)


		self.encodeRadio = tk.Radiobutton(self.actionFrame, text = "Encode", variable = self.actionRadioVar, value = 1)
		self.encodeRadio.config(background = "#DADFDF")
		self.encodeRadio.pack()

		self.decodeRadio = tk.Radiobutton(self.actionFrame, text = "Decode", variable = self.actionRadioVar, value = 2)
		self.decodeRadio.config(background = "#DADFDF")
		self.decodeRadio.pack()


		#Dropdown's (Language and Encryption Alogrithm)
		
		self.languageVar.set(self.languageList[0])
		self.languagedrop = tk.OptionMenu(self.root, self.languageVar, *self.languageList)
		self.languagedrop.config(background = "#DADFDF")
		self.languagedrop.grid(row = 0, column = 2, sticky = 'NSEW')

		self.algorithmVar.set(self.algorithmList[0])
		self.algorithmdrop = tk.OptionMenu(self.root, self.algorithmVar, *self.algorithmList)
		self.algorithmdrop.config(background = "#DADFDF")
		self.algorithmdrop.grid(row = 1, column = 2, sticky = 'NSEW')

		#########


		#Input to Output (Input,Output, Shift, Submit)

		self.inputEnt = tk.Text(self.root, background = "black", foreground = "lime",
									height = 10, width = 65)
		self.inputEnt.config(highlightbackground = "#074C0A")
		self.inputEnt.grid(row = 3, column = 0, columnspan = 4, sticky = 'W', padx = 5, pady = 5)


		self.shiftFrame = tk.LabelFrame(self.root, text = "Shift")
		self.shiftFrame.config(background = "#DADFDF", relief = "sunken")
		self.shiftFrame.grid(row = 4, column = 0, padx = 20)

		self.shiftSpin = tk.Spinbox(self.shiftFrame, from_ = -25, to = 25, width = 8)
		self.shiftSpin.config(background = "#DADFDF", highlightbackground = "#DADFDF")
		self.shiftSpin.pack()

		self.submitbtn = tk.Button(self.root, text = "Submit", width = 25, height = 2)
		self.submitbtn.config(background = "#DADFDF", relief = "sunken", highlightbackground = "#232423")
		self.submitbtn.grid(row = 4, column = 1, columnspan = 2, sticky = 'W', pady = 5)

		self.outputEnt = tk.Text(self.root, background = "black", foreground = "lime",
									height = 10, width = 65)
		self.outputEnt.config(state = "disabled", highlightbackground = "#074C0A")
		self.outputEnt.grid(row = 5, column = 0, columnspan = 4, rowspan = 3, sticky = 'W', padx = 5, pady = 5)

		########


		#Descriptions

		self.algoDesc = tk.Text(self.root, background = "gray", foreground = "white",
										height = 5, width = 50)
		self.algoDesc.config(state = "disabled", highlightbackground = "#232423")
		self.algoDesc.grid(row = 0, column = 6, rowspan = 3)

		self.codeDesc = tk.Text(self.root, background = "gray", foreground = "white",
										height = 10, width = 50)
		self.codeDesc.config(state = "disabled", highlightbackground = "#232423")
		self.codeDesc.grid(row = 3, column = 6)

		########


		#Import Export Buttons

		self.importbtn = tk.Button(self.root, text = "Import to Text File", 
											height = 2, width = 40, command = self.importfnc)
		self.importbtn.config(highlightbackground = "#232423")
		self.importbtn.grid(row = 4, column = 6, padx = 12)

		self.exportbtn = tk.Button(self.root, text = "Export From Text File", 
											height = 2, width = 40, command = self.exportfnc)
		self.exportbtn.config(highlightbackground = "#232423")
		self.exportbtn.grid(row = 5, column = 6)

		###########


		#LOGO
		
		self.logo = tk.PhotoImage(file = "InstaCryptLogo.png")
		self.logoImage = tk.Label(image = self.logo)
		self.logoImage.config(background = "#232423")
		self.logoImage.grid(row = 6, column = 6, sticky = "NW", padx = 12, pady = 10)
		
		#####



		self.root.mainloop()

	def importfnc(self):
		print(self.importbtn["text"])

	def exportfnc(self):
		print(self.exportbtn["text"])







mainPage = Instacrypt()









