import tkinter as tk
def show_msg():
    name = name_entry.get()
    mobile = mobile_entry.get()
    city = city_entry.get()
    msg = f"Welcome {name}! Your Mobile No. is {mobile} and you are from {city}."
    result_label.config(text = msg)
root = tk.Tk()
root.title("Aditya Singh F114")
tk.Label(root, text = "Name :").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text = "Mobile No. :").pack()
mobile_entry = tk.Entry(root)
mobile_entry.pack()
tk.Label(root, text = "City :").pack()
city_entry = tk.Entry(root)
city_entry.pack()
submit_button = tk.Button(root, text = "Submit", command = show_msg)
submit_button.pack()
result_label = tk.Label(root, text = "")
result_label.pack()

root.mainloop()
