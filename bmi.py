import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try: 
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid input", "Weight and height must be greater than 0.")
            return
        
        bmi = weight / (height ** 2)
        bmi_result.config(text=f"Your BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        category_result.config(text=f"Category: {category}")
    
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numerical values.")

window = tk.Tk()
window.title("BMI Calculator")

label_weight = tk.Label(window, text="Enter weight (kg):")
label_weight.grid(row=0, column=0, padx=10, pady=10)

entry_weight = tk.Entry(window)
entry_weight.grid(row=0, column=1, padx=10, pady=10)

label_height = tk.Label(window, text="Enter height (m):")
label_height.grid(row=1, column=0, padx=10, pady=10)

entry_height = tk.Entry(window)
entry_height.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

bmi_result = tk.Label(window, text="Your BMI: ")
bmi_result.grid(row=3, column=0, columnspan=2, pady=10)

category_result = tk.Label(window, text="Category: ")
category_result.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
