import tkinter as tk
from tkinter import ttk
import threading

def on_scale(value):
    current_value_label.config(text=f"Current Volume: {int(float(value))}")
    print(f"Volume set to: {value}")

def run_thru_Thread(target, *args):
    thread = threading.Thread(target=target, args=args)
    thread.start()

# Create the main window
root = tk.Tk()
root.title("Volume Control Example")

# Create a label to display the value
value_label = ttk.Label(root, text="Adjust the volume:")
value_label.pack(pady=10)

# Create a scale (slider) widget
scale = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=lambda value: run_thru_Thread(on_scale, value))
scale.pack(fill=tk.X, padx=20, pady=10)

# Create a label to show the current scale value
current_value_label = ttk.Label(root, text="Current Volume: 0")
current_value_label.pack(pady=10)

# Run the application
root.mainloop()

