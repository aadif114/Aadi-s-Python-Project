import tkinter as tk
from tkinter.ttk import Combobox

def shw_details():
    name = name_entry.get()
    wh = wh_combo.get()
    rollno = rollno_combo.get()
    city = city_combo.get()
    result = f"Name: {name}\nWhole No: {wh}\nRoll No: {rollno}\ncity: {city}"
    result_label.config(text=result)
root = tk.Tk()
root.title("F114 Aditya Singh")
root.geometry("300x300")
tk.Label(root, text = "Enter Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text="Select whole number:").pack()
wh_combo = Combobox(root, values=["1", "2", "3", "4", "5"])
wh_combo.pack()
tk.Label(root, text = "Select Roll No.:").pack()
rollno_combo = Combobox(root, values = ["F111", "F112", "F113", "F114", "F115"])
rollno_combo.pack()
tk.Label(root, text = "Select City:").pack()
city_combo = Combobox(root, values = ["Mumbai", "Delhi", "Dehradun", "Noida", "Pune"])
city_combo.pack()
tk.Button(root, text="Show Details", command=shw_details).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
