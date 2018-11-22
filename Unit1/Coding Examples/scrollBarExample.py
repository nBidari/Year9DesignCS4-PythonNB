import tkinter as tk

root = tk.Tk()

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side='right', fill= 'y')

output = tk.Text(root, width = 50, height = 10, 
			borderwidth = 3, relief=tk.GROOVE, 
		yscrollcommand = scrollbar.set)

output.pack(side='left', fill= 'both')

scrollbar.config(command=output.yview)

root.mainloop()