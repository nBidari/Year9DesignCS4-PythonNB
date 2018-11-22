import tkinter as tk

class Instacrypt:


	def __init__(self):
		self.languageSelect = 0
		self.algorithmSelect = 0

		self.root = tk.Tk()
		self.root.title("InstaCrypt")

		#Action's

		self.actionFrame = tk.LabelFrame(self.root, text = "Action")
		self.actionFrame.grid(row = 0, column = 0, rowspan = 2,columnspan = 2)


		self.encodeRadio = tk.Radiobutton(self.actionFrame, text = "Encode")
		self.encodeRadio.pack()

		self.decodeRadio = tk.Radiobutton(self.actionFrame, text = "Decode")
		self.decodeRadio.pack()
		#########


		#Dropdown's (Language and Encryption Alogrithm)

		self.languageLab = tk.Label(self.root, text = "Language Select")
		self.languageLab.grid(row = 0, column = 2, columnspan = 2)

		self.languagedrop = tk.OptionMenu(self.root, self.languageSelect, 
										"English", "Espanol",
											"Farsi", "Francais")
		self.languagedrop.grid(row = 0, column = 4)


		self.algorithmLab = tk.Label(self.root, text = "Encrpytion Algorithm")
		self.algorithmLab.grid(row = 1, column = 2, columnspan = 2)

		self.algorithmdrop = tk.OptionMenu(self.root, self.algorithmSelect,
										"ASCII", "Binary", "ROTI",
										 "ASCII-Binary", "Binary Inversion")
		self.algorithmdrop.grid(row = 1, column = 4)

		#########


		#Input to Output (Input,Output, Shift, Submit)

		self.inputEnt = tk.Text(self.root, background = "black", foreground = "lime",
									height = 10, width = 65)
		self.inputEnt.grid(row = 3, column = 0, columnspan = 4)

		self.shiftSpin = tk.Spinbox(self.root, from_ = -25, to = 25)
		self.shiftSpin.grid(row = 4, column = 0)

		self.submitbtn = tk.Button(self.root, text = "Submit", width = 25, height = 2)
		self.submitbtn.grid(row = 4, column = 1, columnspan = 2)

		self.outputEnt = tk.Text(self.root, background = "black", foreground = "lime",
									height = 10, width = 65)
		self.outputEnt.config(state = "disabled")
		self.outputEnt.grid(row = 5, column = 0, columnspan = 4, rowspan = 3)

		########


		#Descriptions

		self.algoDesc = tk.Text(self.root, background = "gray", foreground = "white",
										height = 5, width = 50)
		self.algoDesc.config(state = "disabled")
		self.algoDesc.grid(row = 0, column = 6, rowspan = 3)

		self.codeDesc = tk.Text(self.root, background = "gray", foreground = "white",
										height = 10, width = 50)
		self.codeDesc.config(state = "disabled")
		self.codeDesc.grid(row = 3, column = 6)

		#Import Export Buttons

		self.importbtn = tk.Button(self.root, text = "Import to Text File", 
											height = 2, width = 40)
		self.importbtn.grid(row = 6, column = 6)

		self.exportbtn = tk.Button(self.root, text = "Export From Text File", 
											height = 2, width = 40)
		self.exportbtn.grid(row = 7, column = 6)




		self.root.mainloop()



mainPage = Instacrypt()
