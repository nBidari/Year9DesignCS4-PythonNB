import tkinter as tk
import math

def submit():

	print("Submit Pressed")
	r = float(entr.get())
	h = float(enth.get())

	v = math.pi * r * r * h
	v = round(v,3)

	output.config(state = "normal")
	output.insert(tk.INSERT, v)
	output.config(state = "disabled")



root = tk.Tk()
root.title("Volume of a Cylinder")

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