import os
import subprocess
from PIL import ImageGrab
from datetime import datetime
import time
current_dir = os.getcwd()
current_time = datetime.now().strftime('%Y-%m-%d_%H%M%S')

def take_screen_shot(log):
    output_img_name = f"Window_BackGround_{current_time}.png"
    output_img_full_path = os.path.join(current_dir, "imgc_result", output_img_name)
    output_img_path = os.path.join(current_dir, "imgc_result")

    # Example log entry
    log_message = "Taking a Screenshot......"
    log(f'{log_message}', 'info')
    # Get the currently active window
    screenshot = ImageGrab.grab()
    # Save the screenshot to a file
    screenshot.save(output_img_full_path)
    log(f"Screenshot {output_img_name} saved at: \n{output_img_path}","log")
    subprocess.Popen(f'explorer {output_img_path}')

def time_update(self,time_label):
    #current_time = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    current_time = time.strftime("%H:%M:%S")  # Make sure this is defined
    time_label.config(text=f"{current_time}", anchor="center", style="blue.TLabel")
    self.after(1000, lambda: time_update(self, time_label))