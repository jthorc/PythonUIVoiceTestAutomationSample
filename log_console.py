import tkinter as tk
import code
import sys
import traceback
from io import StringIO
from datetime import datetime

class Console(tk.Text):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.current_time = datetime.now().strftime('%Y-%m-%d_%H%M%S')
        self.bind("<Return>", self.on_return)
        self.bind("<Control-Return>", self.on_control_return)

        # Define tags for coloring
        self.tag_configure('log', foreground='blue')
        self.tag_configure('error', foreground='red')
        self.tag_configure('info', foreground='green')
        self.tag_configure('warning', foreground='orange')

        self.prompt = "This is just a Python demo for Shuocheng's Automation tool\nRev:00\nModify date:2024/08/29\nLive Log:\n"
        self.console = code.InteractiveConsole()
        self.output_buffer = StringIO()
        self.update_prompt()

    def update_prompt(self):
        self.append_log(self.prompt, 'info')
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
            self.append_log(output, 'warning')
        self.update_prompt()

    def append_log(self, message, tag=None):
        self.config(state=tk.NORMAL)
        self.insert(tk.END, f'{self.current_time}:{message}\n\n', tag)
        self.config(state=tk.DISABLED)
        self.see(tk.END)