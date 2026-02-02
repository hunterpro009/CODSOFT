import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("400x300")

        self.length_var = tk.StringVar(value="12")
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        self.password_var = tk.StringVar()

        ttk.Label(self.master, text="Password Length:").pack(pady=5)
        ttk.Entry(self.master, textvariable=self.length_var, width=5).pack(pady=5)
        ttk.Checkbutton(self.master, text="Include Uppercase", variable=self.uppercase_var).pack(pady=5)
        ttk.Checkbutton(self.master, text="Include Lowercase", variable=self.lowercase_var).pack(pady=5)
        ttk.Checkbutton(self.master, text="Include Digits", variable=self.digits_var).pack(pady=5)
        ttk.Checkbutton(self.master, text="Include Symbols", variable=self.symbols_var).pack(pady=5)
        ttk.Button(self.master, text="Generate Password", command=self.generate_password).pack(pady=10)
        ttk.Entry(self.master, textvariable=self.password_var, width=30).pack(pady=5)
        ttk.Button(self.master, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=10)

    def generate_password(self):
        length = int(self.length_var.get())
        characters = ""
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.digits_var.get():
            characters += string.digits
        if self.symbols_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("Warning", "Select at least one character type!")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)
        
    def copy_to_clipboard(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.password_var.get())
        self.master.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
    