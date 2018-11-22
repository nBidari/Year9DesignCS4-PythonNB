import tkinter as tk

root = tk.Tk()

w = tk.Spinbox(root, from_=0, to=10)
w.pack()

root.mainloop()