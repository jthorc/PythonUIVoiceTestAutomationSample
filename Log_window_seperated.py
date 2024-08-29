import tkinter as tk
from log_widget import add_log  # Import the add_log class

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Automation Panel")
        self.geometry("650x500")

        # Create the main frame
        main_frame = tk.Frame(self)
        main_frame.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        # Configure rows and columns in the grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        # Create and place the add_log widget (Text widget)
        self.Log = add_log(main_frame, wrap=tk.WORD)
        self.Log.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        # Example usage of append_log method
        self.Log.append_log("This is an info message", 'info')
        self.Log.append_log("This is a warning message", 'warning')
        self.Log.append_log("This is an error message", 'error')

if __name__ == "__main__":
    app = Application()
    app.mainloop()