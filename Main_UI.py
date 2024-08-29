import tkinter as tk
from tkinter import ttk
import code
import sys
import traceback
from io import StringIO
import subprocess
from tkinter import filedialog
import json
import time
import os
import pygetwindow as gw
from PIL import ImageGrab
from datetime import datetime

class Console(tk.Text):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
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
        self.insert(tk.END, f'{Application.current_time}:{message}\n\n', tag)
        self.config(state=tk.DISABLED)
        self.see(tk.END)

class Application(tk.Tk):
    current_dir = os.getcwd()
    current_time = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    def __init__(self):
        super().__init__()

        self.title("Automation Panel")
        self.geometry("650x500")

        # Create the main frame
        main_frame = ttk.Frame(self)
        main_frame.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        # Configure rows and columns in the grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        # Create a Label widget
        #label_0 = tk.Label(main_frame, text="Log:", font=("bold"), fg="Black")
        # Place the Label in the window
        #label_0.grid(row=0, column=0, sticky="W")

        # Create the combined log and console window (Text widget)
        self.console = Console(main_frame, wrap=tk.WORD)
        self.console.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        # Create buttons and place them in the grid
        log_button = ttk.Button(main_frame, text="Take Screen Shot", command=self.take_screen_shot)
        log_button.grid(row=2, column=0, padx=5, pady=5,sticky="nsew")

        clear_button = ttk.Button(main_frame, text="Clear Log", command=self.clear_log_entry)
        clear_button.grid(row=2, column=1, padx=5, pady=5,sticky="nsew")

        adb_button = ttk.Button(main_frame, text="Check ADB Connection", command=self.check_adb_connection)
        adb_button.grid(row=2, column=2, padx=5, pady=5,sticky="nsew")

        read_button = ttk.Button(main_frame, text="Read Test Procedure", command=self.read_test_procedure)
        read_button.grid(row=2, column=3, padx=5, pady=5,sticky="nsew")

        check_system_time = ttk.Button(main_frame, text="Check Sys Time", command=self.check_sys_time)
        check_system_time.grid(row=2, column=4, padx=5, pady=5,sticky="nsew")

    def take_screen_shot(self):
        output_img_name = f"Window_BackGround_{self.current_time}.png"
        output_img_full_path = os.path.join(self.current_dir, "imgc_result", output_img_name)
        output_img_path = os.path.join(self.current_dir, "imgc_result")

        # Example log entry
        log_message = "Taking a Screenshot......"
        self.console.append_log(f'{log_message}', 'info')
        # Get the currently active window
        screenshot = ImageGrab.grab()
        # Save the screenshot to a file
        screenshot.save(output_img_full_path)
        self.console.append_log(f"Screenshot {output_img_name} saved at: \n{output_img_path}","log")
        subprocess.Popen(f'explorer {output_img_path}')
        '''
        active_window = gw.getActiveWindow()
        if active_window:
            # Get the bounding box of the active window
            bbox = (active_window.left, active_window.top, active_window.right, active_window.bottom)
            # Capture the screenshot of the active window
            screenshot = ImageGrab.grab(bbox)
            # Save the screenshot to a file
            screenshot.save(output_img_full_path)
            self.console.append_log(f"Screenshot {output_img_full_path} saved at: \n{output_img_path}","log")
            subprocess.Popen(f'explorer {output_img_path}')
        
        else:
            self.console.append_log("No active window found.","log")
        '''
    def clear_log_entry(self):
        # Clear the messages in the combined window
        self.console.config(state=tk.NORMAL)
        self.console.delete(1.0, tk.END)
        self.console.config(state=tk.DISABLED)
    
    def read_test_procedure(self):
        initial_directory = os.getcwd()
        # Open file dialog to select a JSON file
        file_path = filedialog.askopenfilename(
            initialdir=initial_directory,
            title="Select a JSON file",
            filetypes=[("JSON files", "*.json")],
        )

        if file_path:
            try:
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    self.console.append_log("JSON data loaded successfully:",'info')
                    self.console.append_log(data, 'log')
                    return data  # Returns the dictionary
            except json.JSONDecodeError as e:
                self.console.append_log(f"Error decoding JSON: {e}",'error')
            except Exception as e:
                self.console.append_log(f"An error occurred: {e}",'error')
        else:
            self.console.append_log("No file was selected.", 'warning')

    def check_sys_time(self):
        try:
            # Get the current local time
            current_time = datetime.now()
            # Get the time zone offset from UTC (in seconds)
            time_zone_offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
            time_zone_offset_hours = time_zone_offset / 3600  # Convert to hours
            # Get the name of the time zone
            time_zone_name = time.tzname
            self.console.append_log(f"Current Time: {current_time}\nTime Zone Offset (in hours): {time_zone_offset_hours}\nTime Zone Name: {time_zone_name}\n", 'info')
        except Exception as e:
            self.console.append_log(f'error: {e}','error')



    def check_adb_connection(self):
        command = ['adb', 'devices']
        command_title = 'Running adb command: ' 
        self.console.append_log(f'{command_title} {command}', 'info')
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            output = result.stdout
        except subprocess.CalledProcessError as e:
            output = f"Error checking ADB connection: {e}\n{e.output}"
            self.console.append_log(output, 'error')
            return
        
        # Append ADB connection status to the console
        self.console.append_log(f"ADB Connection Status:\n{output}", 'log')



if __name__ == "__main__":
    app = Application()
    app.mainloop()