import tkinter as tk

master = tk.Tk()

v = 0

button = tk.Radiobutton(master, text="One",
			 variable=v, value=1)
button.pack()

buttonTwo = tk.Radiobutton(master, text="Two", 
			 variable=v, value=2)
buttonTwo.pack()

master.mainloop()