# log_widget.py
import tkinter as tk

class add_log(tk.Text):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.tag_configure('log', foreground='blue')
        self.tag_configure('error', foreground='red')
        self.tag_configure('info', foreground='green')
        self.tag_configure('warning', foreground='orange')

    def append_log(self, message, tag=None):
        self.config(state=tk.NORMAL)
        self.insert(tk.END, f'{message}\n\n', tag)
        self.config(state=tk.DISABLED)
        self.see(tk.END)