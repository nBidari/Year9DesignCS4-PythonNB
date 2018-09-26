import tkinter as tk
import math

def submit():

	print("Submit Pressed")
	r = float(entr.get())
	h = float(enth.get())

	v = math.pi * r * r * h
	v = round(v,3)

	output.config(state = "normal")

	outputValue = "Given:\nRadius: " + str(r) + " units\nHeight: " + str(h) + " units\nThe Volume is: " + str(v) +" units cubed \n \n \n \n \n \n" + str(accessibility)

	output.insert(tk.INSERT, outputValue)
	output.config(state = "disabled")


accessibility = 0


root = tk.Tk()
root.title("Volume of a Cylinder")

chkBtn = tk.Radiobutton(root, text = "Accessibility", variable = accessibility)
chkBtn.pack()

labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="submit", command=submit)
btn.pack()

output = tk.Text(root, width = 50, height = 10, borderwidth = 3, relief=tk.GROOVE)
output.pack()




root.mainloop() 






