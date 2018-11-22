import tkinter as tk

master = tk.Tk()

group = tk.LabelFrame(master, text="Group", padx=5, pady=5)
group.pack(padx=10, pady=10)

w = tk.Entry(group)
w.pack()

y = tk.Entry(group)
y.pack()

tk.mainloop()