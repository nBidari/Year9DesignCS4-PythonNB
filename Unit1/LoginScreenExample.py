import tkinter as tk

#With the login page all elements are vertically aligned
#So I am just going to use pack.

#Main Window
root = tk.Tk() #creates the standard main window.
#Tk() is a special function called a constructor
#If a function is written with a capital letter
#it indicates it is a constructor

#CONSTRUCT
#CONFIGURE
#PACK | Put into the window

#We are writing an EVENT DRIVEN PROGRAM.
#Build the GUI
#Start it running
#Wait for "EVENT"

#LABELFRAME
frame = tk.LabelFrame(root, text = "Login")
frame.pack()

##USERNAME
labUN = tk.Label(frame, text = "Username")
#Ordered parameters: The order we send them matters.
#Named Parameters: Javascript and Python specific
                  #Given a name so that it is obvious
                  #what to do with it
labUN.pack()

entUN = tk.Entry(frame)
entUN.config(bg = "gray")
entUN.pack()



##PASSWORD
labPass = tk.Label(frame, text = "Password")
labPass.pack()

entPass = tk.Entry(frame, show = "*")
entPass.config(bg = "gray")
entPass.pack()


##SUBMIT
btnSubmit = tk.Button(root, text = "Submit")
btnSubmit.pack()

root.mainloop()

