import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title("Multiple Selection Example")
window.geometry("400x400")

# Add a label
label = ttk.Label(window, text="Select items from the list:")
label.pack(pady=10)

# Add a Listbox with multiple selection enabled
listbox = tk.Listbox(window, selectmode=tk.MULTIPLE)  # MULTIPLE for multiple selections
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# Add items to the Listbox
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
for item in items:
    listbox.insert(tk.END, item)

# Add a text entry area with a default value
entry_label = ttk.Label(window, text="Type something:")
entry_label.pack(pady=10)

text_entry = ttk.Entry(window)
text_entry.insert(0, "default")  # Set the default value
text_entry.pack(pady=10, fill=tk.X)

# Add a label to show the selected items
result_label = ttk.Label(window, text="Selected: None", background="lightgray")
result_label.pack(pady=10, fill=tk.X)

# Add a button to get the selected items and entry value
def show_selected_items():
    selected_indices = listbox.curselection()  # Get selected indices
    typed_text = text_entry.get()  # Get the text from the entry
    
    if selected_indices:
        selected_items = [listbox.get(i) for i in selected_indices]  # Get all selected items
        result_label.config(text=f"Selected: {', '.join(selected_items)}, Typed: {typed_text}")
    else:
        result_label.config(text=f"No items selected, Typed: {typed_text}")

button = ttk.Button(window, text="Show Selected", command=show_selected_items)
button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
