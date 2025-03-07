import tkinter as tk
from tkinter import messagebox
from tkinter import Entry, Button, Label
import random
import string
import pyperclip

class PasswordGenerator:
    def _init_(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("400x300")  # Set the window size

        self.label_length = Label(self.root, text="Password Length:", font=("Arial", 12))
        self.label_length.pack(pady=10)
        self.entry_length = Entry(self.root, font=("Arial", 12))
        self.entry_length.pack(pady=5)

        self.include_letters = tk.IntVar()
        self.include_numbers = tk.IntVar()
        self.include_symbols = tk.IntVar()

        self.checkbox_letters = tk.Checkbutton(self.root, text="Include Letters", variable=self.include_letters, font=("Arial", 12))
        self.checkbox_letters.pack(pady=5)
        self.checkbox_numbers = tk.Checkbutton(self.root, text="Include Numbers", variable=self.include_numbers, font=("Arial", 12))
        self.checkbox_numbers.pack(pady=5)
        self.checkbox_symbols = tk.Checkbutton(self.root, text="Include Symbols", variable=self.include_symbols, font=("Arial", 12))
        self.checkbox_symbols.pack(pady=5)

        self.generate_button = Button(self.root, text="Generate Password", command=self.generate_password, font=("Arial", 12), bg="lightblue")
        self.generate_button.pack(pady=10)

        self.password_result = Label(self.root, text="", font=("Arial", 12, "bold"))
        self.password_result.pack(pady=10)

        self.copy_button = Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard, font=("Arial", 12), bg="lightgreen")
        self.copy_button.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.entry_length.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the password length.")
            return

        include_letters = self.include_letters.get()
        include_numbers = self.include_numbers.get()
        include_symbols = self.include_symbols.get()

        if not include_letters and not include_numbers and not include_symbols:
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        characters = ''
        if include_letters:
            characters += string.ascii_letters
        if include_numbers:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_result.config(text=f"Generated Password: {password}")

    def copy_to_clipboard(self):
        password = self.password_result.cget("text").split(": ")[1]
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard.")

if _name_ == "_main_":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()