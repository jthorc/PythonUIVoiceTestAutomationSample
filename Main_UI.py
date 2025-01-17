import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import filedialog
import json
import time
import os
#from PIL import ImageGrab
from datetime import datetime
from log_console import Console

GLOBAL_VALUE = 'global value'
# Set the working directory to the directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Application(tk.Tk):
    current_dir = os.getcwd()
    current_time = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    def __init__(self):
        super().__init__()

        self.title("Automation Panel")

        # Create the combined log and console window (Text widget)
        self.console = Console(self, wrap=tk.WORD)
        self.console.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")
        self.log = self.console.append_log

        # Create buttons and place them in the grid
        clear_button = ttk.Button(self, text="Clear Log", command=self.clear_log_entry)
        clear_button.grid(row=2, column=0, padx=5, pady=5,sticky="nsew")

        notebook = ttk.Notebook(self)
        notebook.grid(row=3, column=0, columnspan=5, padx=5, pady=5,sticky="nsew")

        # Create tabs
        self.operation_tab(notebook, "Operation")
        self.communication_tab(notebook, "Communication")
        self.test_tab(notebook, "Test")
        self.log(f"Running at:{self.current_dir}","info")


    def operation_tab(self,notebook, tab_name):
        # Create a frame for the tab
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=tab_name)
        #log_button = ttk.Button(frame, text="Take Screen Shot", command=self.take_screen_shot)
        #log_button.grid(row=0, column=0, padx=5, pady=5,sticky="nsew")
        check_system_time = ttk.Button(frame, text="Check Sys Time", command=self.check_sys_time)
        check_system_time.grid(row=0, column=1, padx=5, pady=5,sticky="nsew")

    def communication_tab(self,notebook, tab_name):
        # Create a frame for the tab
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=tab_name)
        adb_button = ttk.Button(frame, text="Check ADB Connection", command=self.check_adb_connection)
        adb_button.grid(row=0, column=0, padx=5, pady=5,sticky="nsew")

    def test_tab(self,notebook, tab_name):
        # Create a frame for the tab
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=tab_name)
        read_button = ttk.Button(frame, text="Read Test Procedure", command=self.read_test_procedure)
        read_button.grid(row=0, column=0, padx=5, pady=5,sticky="nsew")

        # Add a label
        label = ttk.Label(frame, text="Select an item from the list:")
        label.grid(row=1, column=0, padx=5, pady=5,sticky="nsew")

        # Add a Listbox
        listbox = tk.Listbox(frame, selectmode=tk.SINGLE,exportselection=False)  # SINGLE for single selection
        listbox.grid(row=2, column=0, padx=5, pady=5,sticky="nsew")

        selection_mode_var = tk.BooleanVar(value=False)  # Start with MULTIPLE mode

        def toggle_selection_mode():
            if selection_mode_var.get()==True:
                listbox.config(selectmode=tk.MULTIPLE)
            else:
                listbox.config(selectmode=tk.SINGLE)

        checkbox = ttk.Checkbutton(frame, text="Multiple Selection", variable=selection_mode_var, command=toggle_selection_mode)
        checkbox.grid(row=2, column=2, padx=5, pady=5, sticky="w")



        # Add items to the Listbox
        items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5","Item 6", "Item 7", "Item 8", "Item 9", "Item 10","Item 11", "Item 12", "Item 13", "Item 14", "Item 15"]
        for item in items:
            listbox.insert(tk.END, item)

        # Add a label to show the selected item
        result_label = ttk.Label(frame, text="Selected: None", background="lightgray")
        result_label.grid(row=3, column=0, columnspan=5, padx=5, pady=5,sticky="nsew")

        text_entry = ttk.Entry(frame)
        text_entry.insert(0, "default")  # Set the default value
        text_entry.grid(row=4, column=0, padx=5, pady=5,sticky="nsew")

        # Add a button to get the selected item
        def show_selected_item():
            selected_indices = listbox.curselection()  # Get selected indices
            if selected_indices:
                selected_item = [listbox.get(i) for i in selected_indices]  # Get the selected item
                typed_text = text_entry.get()  # Get the text from the entry
                result_label.config(text=f"Selected: {selected_item}, Typed: {typed_text}")
            else:
                result_label.config(text=f"Selected: None, Typed: None")

        #button = ttk.Button(frame, text="Show Selected", command=lambda:show_selected_item)
        button = ttk.Button(frame, text="Show Selected", command=show_selected_item)
        button.grid(row=4, column=1, padx=5, pady=5,sticky="nsew")


    '''
    def take_screen_shot(self):
        output_img_name = f"Window_BackGround_{self.current_time}.png"
        output_img_full_path = os.path.join(self.current_dir, "imgc_result", output_img_name)
        output_img_path = os.path.join(self.current_dir, "imgc_result")

        # Example log entry
        log_message = "Taking a Screenshot......"
        self.log(f'{log_message}', 'info')
        # Get the currently active window
        screenshot = ImageGrab.grab()
        # Save the screenshot to a file
        screenshot.save(output_img_full_path)
        self.log(f"Screenshot {output_img_name} saved at: \n{output_img_path}","log")
        subprocess.Popen(f'explorer {output_img_path}')
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
                    self.log("JSON data loaded successfully:",'info')
                    self.log(data, 'log')
                    return data  # Returns the dictionary
            except json.JSONDecodeError as e:
                self.log(f"Error decoding JSON: {e}",'error')
            except Exception as e:
                self.log(f"An error occurred: {e}",'error')
        else:
            self.log("No file was selected.", 'warning')

    def check_sys_time(self):
        try:
            # Get the current local time
            current_time = datetime.now()
            # Get the time zone offset from UTC (in seconds)
            time_zone_offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
            time_zone_offset_hours = time_zone_offset / 3600  # Convert to hours
            # Get the name of the time zone
            time_zone_name = time.tzname
            self.log(f"Current Time: {current_time}\nTime Zone Offset (in hours): {time_zone_offset_hours}\nTime Zone Name: {time_zone_name}\n", 'info')
        except Exception as e:
            self.log(f'error: {e}','error')



    def check_adb_connection(self):
        command = ['adb', 'devices']
        command_title = 'Running adb command: ' 
        self.log(f'{command_title} {command}', 'info')
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            output = result.stdout
            # Append ADB connection status to the console
            self.log(f"ADB Connection Status:\n{output}", 'log')
            
            if len(output)>26:
                return True
            else:
                return False
        except Exception as e:
            #output = f"Error checking ADB connection: {e}\n{e.output}"
            self.log(e, 'error')
            return False
        
if __name__ == "__main__":
    app = Application()
    app.mainloop()