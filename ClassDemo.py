import tkinter as tk

#Classes: A blueprint to make objects
#Object: An instance of the calss

#Three Parts

#Constructors: This is a special method run only once when we instantiate
#Attributes: These are variabls that describe the state of the object.
#Behaviours: These are functions that can be called that deal with the object.

#Attributes are variables
#Behaviours of Functions

class LoginPage():
	#The first thing is always the constructor all the code that
	#you write now will be put in the constructor

	def __init__(self):
		print("Running Constructor")
		self.root = tk.Tk()

		self.frame = tk.LabelFrame(self.root, text = "Login")
		self.frame.pack()
		
		self.labUN = tk.Label(self.frame, text = "Username")
		self.labUN.pack()
		
		self.entUN = tk.Entry(self.frame)
		self.entUN.config(bg = "gray")
		self.entUN.pack()
		
		self.labPass = tk.Label(self.frame, text = "Password")
		self.labPass.pack()
		
		self.entPass = tk.Entry(self.frame, show = "*")
		self.entPass.config(bg = "gray")
		self.entPass.pack()
		
		self.btnSubmit = tk.Button(self.root, text = "Submit", command = self.clicked)
		self.btnSubmit.pack()


		self.root.mainloop()
		
	def clicked(self):
		print("clicked")
	

mainpage = LoginPage() #This fcreates an instance of the class

'''
root = tk.Tk()
frame = tk.LabelFrame(root, text = "Login")
frame.pack()
labUN = tk.Label(frame, text = "Username")
labUN.pack()
entUN = tk.Entry(frame)
entUN.config(bg = "gray")
entUN.pack()
labPass = tk.Label(frame, text = "Password")
labPass.pack()
entPass = tk.Entry(frame, show = "*")
entPass.config(bg = "gray")
entPass.pack()
btnSubmit = tk.Button(root, text = "Submit")
btnSubmit.pack()


root.mainloop()
'''
