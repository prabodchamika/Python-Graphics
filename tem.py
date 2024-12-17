import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius}°C = {fahrenheit:.2f}°F")
    except ValueError:
        result_label.config(text="Enter a valid number.")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
    except ValueError:
        result_label.config(text="Enter a valid number.")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")
root.configure(bg="#1C1C1E")  

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", background="#2C2C2E", foreground="white", font=("Helvetica", 12), padding=5)
style.map("TButton", background=[("active", "#3A3A3C")])
style.configure("TLabel", background="#1C1C1E", foreground="white", font=("Helvetica", 12))

title_label = ttk.Label(root, text="Temperature Converter", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

entry = ttk.Entry(root, font=("Helvetica", 14), justify="center")
entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#1C1C1E")
button_frame.pack(pady=10)

c_to_f_button = ttk.Button(button_frame, text="Celsius to Fahrenheit", command=celsius_to_fahrenheit)
c_to_f_button.grid(row=0, column=0, padx=10)

f_to_c_button = ttk.Button(button_frame, text="Fahrenheit to Celsius", command=fahrenheit_to_celsius)
f_to_c_button.grid(row=0, column=1, padx=10)

result_label = ttk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

footer_label = ttk.Label(root, text="Developed by Prabod Chamika", font=("Helvetica", 10, "italic"))
footer_label.pack(side="bottom", pady=10)

root.mainloop()
