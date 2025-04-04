import tkinter as tk
from tkinter import ttk
import time

def time_update(self, label):
    current_time = time.strftime("%H:%M:%S")

    # Alternate style based on seconds (just for demo purposes)
    current_style = "red.TLabel" if int(time.strftime("%S")) % 2 == 0 else "blue.TLabel"

    label.config(text=current_time, style=current_style)
    self.after(1000, lambda: time_update(self, label))

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Styled Clock")
        self.geometry("300x100")

        # Use ttk style system
        style = ttk.Style(self)
        style.configure("red.TLabel", background="red", foreground="white", font=("Arial", 20))
        style.configure("blue.TLabel", background="#87CEEB", foreground="black", font=("Arial", 20))

        self.label = ttk.Label(self, text="", style="red.TLabel", anchor="center")
        self.label.pack(expand=True, fill="both", padx=20, pady=20)

        time_update(self, self.label)

if __name__ == "__main__":
    app = App()
    app.mainloop()