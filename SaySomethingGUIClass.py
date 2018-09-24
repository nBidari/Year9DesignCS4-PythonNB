#Attributes and Behaviours
import os				#os is a module that allows python to run terminal commands
import tkinter as tk 	#tkinter is a module that stores
						#built in functions to create
						#GUI interfaces. 

#A class is a programming structure that allows the programmer to create Objects
#A class is a blueprint and an object is instance of the class. 
#The blueprints for a bike are the class and any bike made from the blueprints is an object
#Classes have 
#
#	Attributes (fields/variables): characteristics used to descibe the object -> Bike Attribute: Gear
#	Behaviours (functions/methods): actions the object can take --> Bike Behaviour: ChangeGear
#
#		
#
class Display:

	#Constructor: Is a special method called only once
	#when I instantiate (create) the object for the first
	#time. 
	def __init__(self):

		print("Running display constructor")
		#instance variables (attribute) in python are self.<variable name>
		self.root = tk.Tk() #Tk is the constructor that builds a basic window

		#To add elements we have to construct them then pack them
		#constructs elements
		self.ent = tk.Entry(self.root) #create Entry object called self.ent
		self.btn = tk.Button(self.root, text = "Speak", command=self.runMe) #create Button object called self.btn

		#pack elements: Pack is the most basic geometry manager
		self.ent.pack()
		self.btn.pack()

		self.root.mainloop()
		print("program end")

	#runMe is an instance method (behaviour), we need to put self as an attribute 
	#for all instance methods. 
	def runMe(self):
		print("Running")
		statement = self.ent.get() #get is an intance method of an Entry object
		os.system("say "+statement)



#Start of program
d = Display() #Creates a display object called d.  It runs the 
			  #constructor
