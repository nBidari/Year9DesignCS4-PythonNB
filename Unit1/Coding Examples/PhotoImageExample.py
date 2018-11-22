import tkinter as tk

root = tk.Tk()
image = tk.PhotoImage(file= "Example.png")
label = tk.Label(image=image)
label.pack()

root.mainloop()