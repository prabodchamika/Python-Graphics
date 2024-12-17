import tkinter as tk
from tkinter import messagebox
from math import *

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#222222")       
        
        self.expression = ""
        self.input_text = tk.StringVar()      
       
        self.root.bind("<Key>", self.key_input)
        self.root.bind("<Return>", lambda event: self.calculate_result())
        self.root.bind("<BackSpace>", lambda event: self.backspace())
        
        self.create_widgets()

    def create_widgets(self):
        
        entry_frame = tk.Frame(self.root, bg="#222222")
        entry_frame.pack(expand=True, fill="both")

        entry = tk.Entry(entry_frame, font=("Helvetica", 28), 
                         textvariable=self.input_text, justify="right", 
                         bd=0, bg="#222222", fg="white")
        entry.pack(expand=True, fill="both", padx=10, pady=10)       
        
        button_frame = tk.Frame(self.root, bg="#222222")
        button_frame.pack(expand=True, fill="both")
        
        buttons = [
            ("C", 1, 0, "#ff3b30", "white"), ("(", 1, 1, "#505050", "white"), 
            (")", 1, 2, "#505050", "white"), ("/", 1, 3, "#ff9500", "white"),
            ("7", 2, 0, "#333333", "white"), ("8", 2, 1, "#333333", "white"), 
            ("9", 2, 2, "#333333", "white"), ("*", 2, 3, "#ff9500", "white"),
            ("4", 3, 0, "#333333", "white"), ("5", 3, 1, "#333333", "white"), 
            ("6", 3, 2, "#333333", "white"), ("-", 3, 3, "#ff9500", "white"),
            ("1", 4, 0, "#333333", "white"), ("2", 4, 1, "#333333", "white"), 
            ("3", 4, 2, "#333333", "white"), ("+", 4, 3, "#ff9500", "white"),
            ("0", 5, 0, "#333333", "white"), (".", 5, 1, "#333333", "white"), 
            ("sqrt", 5, 2, "#505050", "white"), ("=", 5, 3, "#ff9500", "white")
        ]
        
        for (text, row, col, bg_color, fg_color) in buttons:
            button = tk.Button(button_frame, text=text, font=("Helvetica", 18), 
                               fg=fg_color, bg=bg_color,
                               activebackground="#666666", activeforeground=fg_color,
                               command=lambda txt=text: self.on_button_click(txt),
                               relief="flat", bd=0, highlightthickness=0)
            
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            button.configure(height=2, width=6)
            button.bind("<Enter>", lambda e, btn=button: btn.configure(bg="#555555"))
            button.bind("<Leave>", lambda e, btn=button: btn.configure(bg=bg_color))
        
        for i in range(6):
            button_frame.rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.columnconfigure(j, weight=1)

    def on_button_click(self, char):
     
        if char == "sqrt":
            self.expression += "sqrt("
        elif char == "C":
            self.clear()
        elif char == "=":
            self.calculate_result()
        else:
            self.expression += str(char)
        
        self.input_text.set(self.expression)

    def calculate_result(self):
       
        try:
            result = eval(self.expression)
            self.input_text.set(str(result))
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            self.expression = ""

    def clear(self):
        
        self.expression = ""
        self.input_text.set("")
    
    def backspace(self):
       
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

    def key_input(self, event):
  
        key = event.char
        
        if key.isdigit() or key in ".+-*/()":
            self.expression += key
        elif key == '\r':  
            self.calculate_result()
        elif key == '^':
            self.expression += '**'
        elif key == 'c' or key == 'C':
            self.clear()
        elif key == 's':
            self.expression += "sin(radians("
        elif key == 'S':
            self.expression += "sqrt("
        elif key == 'l':
            self.expression += "log("
        elif key == 't':
            self.expression += "tan(radians("
        elif key == 'f':
            self.expression += "factorial("
        
        self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop()
