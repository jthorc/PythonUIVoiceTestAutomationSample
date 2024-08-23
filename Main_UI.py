import tkinter as tk
from tkinter import ttk
import code
import sys
import traceback
from io import StringIO
import subprocess

class Console(tk.Text):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Return>", self.on_return)
        self.bind("<Control-Return>", self.on_control_return)

        # Define tags for coloring
        self.tag_configure('log', foreground='blue')
        self.tag_configure('error', foreground='red')
        self.tag_configure('info', foreground='green')

        self.prompt = "Live Log: "
        self.console = code.InteractiveConsole()
        self.output_buffer = StringIO()
        self.update_prompt()

    def update_prompt(self):
        self.insert(tk.END, self.prompt)
        self.mark_set(tk.INSERT, tk.END)
        self.see(tk.END)

    def on_return(self, event):
        input_text = self.get("insert linestart", tk.INSERT).strip()
        if input_text:
            self.execute(input_text)
        return "break"

    def on_control_return(self, event):
        # For multi-line input, add functionality if needed
        return "break"

    def execute(self, command):
        self.output_buffer.truncate(0)
        self.output_buffer.seek(0)

        # Redirect stdout and stderr
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = self.output_buffer
        sys.stderr = self.output_buffer

        try:
            self.console.push(command)
        except Exception as e:
            traceback.print_exc()
        
        # Reset stdout and stderr
        sys.stdout = old_stdout
        sys.stderr = old_stderr

        output = self.output_buffer.getvalue()
        if output:
            self.insert(tk.END, output, 'info')
        self.update_prompt()

    def append_log(self, message, tag=None):
        self.config(state=tk.NORMAL)
        self.insert(tk.END, message, tag)
        self.config(state=tk.DISABLED)
        self.see(tk.END)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter Combined Console and Log Window")
        self.geometry("600x500")

        # Create the main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create the combined log and console window (Text widget)
        self.console = Console(main_frame, wrap=tk.WORD)
        self.console.pack(fill=tk.BOTH, expand=True)

        # Create a button to add a log message (placed above the console)
        log_button = ttk.Button(main_frame, text="Add Log Entry", command=self.add_log_entry)
        log_button.pack(side=tk.LEFT, pady=10)

        # Create a button to clear the log message (placed beside the log button)
        clear_button = ttk.Button(main_frame, text="Clear Log Entry", command=self.clear_log_entry)
        clear_button.pack(side=tk.LEFT, pady=10)

        # Create a button to check ADB connection
        adb_button = ttk.Button(main_frame, text="Check ADB Connection", command=self.check_adb_connection)
        adb_button.pack(side=tk.LEFT, pady=10)

    def add_log_entry(self):
        # Example log entry
        log_message = "This is a log message.\n"
        self.console.append_log(log_message, 'log')

    def clear_log_entry(self):
        # Clear the messages in the combined window
        self.console.config(state=tk.NORMAL)
        self.console.delete(1.0, tk.END)
        self.console.config(state=tk.DISABLED)

    def check_adb_connection(self):
        try:
            result = subprocess.run(['adb', 'devices'], capture_output=True, text=True, check=True)
            output = result.stdout
        except subprocess.CalledProcessError as e:
            output = f"Error checking ADB connection: {e}\n{e.output}"
            self.console.append_log(output, 'error')
            return
        
        # Append ADB connection status to the console
        self.console.append_log("ADB Connection Status:\n", 'log')
        self.console.append_log(output, 'info')

if __name__ == "__main__":
    app = Application()
    app.mainloop()