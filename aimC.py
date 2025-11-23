import tkinter as tk
from tkinter import messagebox

def check_age():
    try:
        age = int(age_entry.get())
        
        if age < 13:
            result = "Minor"
        elif age >= 13 and age <= 19:
            result = "Teenager"
        elif age >= 20 and age < 60:
            result = "Adult"
        else:
            result = "Senior Citizen"
        
        messagebox.showinfo("Result", f"The person is a {result}.")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

window = tk.Tk()
window.title("F114 Aditya Singh")
window.geometry("300x200")

label = tk.Label(window, text="Enter Age:", font=("Arial", 12))
label.pack(pady=10)

age_entry = tk.Entry(window, font=("Arial", 12))
age_entry.pack()

btn = tk.Button(window, text="Check", font=("Arial", 12), command=check_age)
btn.pack(pady=20)

window.mainloop()
