import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="hello")
button = tk.Button(text= "Roll", width = 10, height = 5)
entry = tk.Entry()
greeting.pack()
entry.pack()
button.pack()
name = entry.get()
window.mainloop()
