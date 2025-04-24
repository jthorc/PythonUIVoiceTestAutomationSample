import json
from tkinter import Tk, Label, Entry, Button, messagebox
import os

class ConfigEditor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = self.load_config()
        self.entries = {}

    def load_config(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load configuration: {e}")
            return {}

    def save_config(self):
        try:
            with open(self.file_path, "w") as file:
                json.dump(self.config, file, indent=4)
            messagebox.showinfo("Success", "Configuration saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save configuration: {e}")

    def update_config(self):
        for key in self.entries:
            self.config[key] = self.entries[key].get()
        self.save_config()

    def create_gui(self):
        root = Tk()
        root.title("Edit Configuration")

        row = 0
        for key, value in self.config.items():
            Label(root, text=key).grid(row=row, column=0)
            entry = Entry(root)
            entry.insert(0, str(value))
            entry.grid(row=row, column=1)
            self.entries[key] = entry
            row += 1

        Button(root, text="Save Changes", command=self.update_config).grid(row=row, columnspan=2)

        root.mainloop()

# Usage
current_path = os.path.dirname(os.path.abspath(__file__))
config_file = "Test_Precedure.Json"
full_path = os.path.join(current_path, config_file)
print(full_path)
editor = ConfigEditor(full_path)
editor.create_gui()
