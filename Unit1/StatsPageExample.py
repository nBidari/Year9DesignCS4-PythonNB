import tkinter as tk

root = tk.Tk()

output = tk.Text(root, background = "gray", height = 10, width = 50)
output.config(state = "disabled")
output.grid(row = 0, column = 0, columnspan = 2)


statone = tk.Button(root, text = "Stat 1")
statone.grid(row = 1, column = 0)

stattwo = tk.Button(root, text = "Stat 2")
stattwo.grid(row = 2, column = 0)

statthree = tk.Button(root, text = "Stat 3")
statthree.grid(row = 3, column = 0)



ascendRadio = tk.Radiobutton(root, text = "Ascend ")
ascendRadio.grid(row = 1, column = 1)

DescendRadio = tk.Radiobutton(root, text = "Descend")
DescendRadio.grid(row = 2, column = 1)



reduceBtn = tk.Button(root, text = "Reduce")
reduceBtn.grid(row = 3, column = 1)


root.mainloop()
