import tkinter as tk

root = tk.Tk()

variable = 0

w = tk.OptionMenu(root, variable, "one", "two", "three")
w.pack()

root.mainloop()