import tkinter as tk

root = tk.Tk() #TK is a constructor
			   #A constructor is a special method only called
			   #It sets everything up for us






lab = tk.Label(root, text = "Enter a number: ")
#To pack a element using the grid geometry manager. We use
# <object>.grid(<parameters>)

lab.grid(row = 0, column = 0)

ent = tk.Entry(root)
ent.grid(row = 1, column = 0)

btn = tk.Button(root, text = "Press Me")
btn.grid(row = 2, column = 0)

output = tk.Text(root)
output.config(state = "disable", bg = "black")
output.grid(row = 0, column = 1, rowspan = 3)

root.mainloop()