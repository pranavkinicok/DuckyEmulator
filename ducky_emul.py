import tkinter as tk
from tkinter import ttk, filedialog, Menu, scrolledtext
import pyautogui
import time
import os

# ...
root = tk.Tk()
root.title("DuckyScript Emulator")


ICON_PATH = os.path.join(os.path.dirname(__file__), 'assets', 'ducky_emul.ico')
root.iconbitmap(ICON_PATH)

class ClosableTab(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.text = tk.StringVar(value="Tab")
        self.label = ttk.Label(self, textvariable=self.text)
        self.label.pack(side="left")

        close_button = ttk.Button(self, text="X", command=self.close_tab)
        close_button.pack(side="right")

    def close_tab(self):
        self.destroy()
        # Add any other cleanup code here if needed

# ...

def new_tab():
    frame = ClosableTab(notebook)
    notebook.add(frame, text="Tab")
    txt_input = scrolledtext.ScrolledText(frame, wrap=tk.WORD)
    txt_input.pack(expand=True, fill='both')
    frame.text.set(f"Tab {len(notebook.tabs())}")


# Basic emulate function
def emulate_duckyscript(script):
    commands = script.split('\n')
    for command in commands:
        cmd = command.strip().split(' ')
        action = cmd[0].lower()

        if action == "rem":
            continue
        elif action == "delay":
            time.sleep(float(cmd[1]) / 1000)
        elif action == "string":
            pyautogui.write(' '.join(cmd[1:]))
        elif action == "enter":
            pyautogui.press('enter')
        elif action == "windows" or action == "gui":
            pyautogui.hotkey('win', cmd[1].lower())
        elif action == "ctrl":
            pyautogui.hotkey('ctrl', cmd[1].lower())
        # ... Add other DuckyScript commands as needed





# Notebook widget to handle multiple tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Creating a frame for the first tab
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text="Untitled 1")

# Adding a scrolled text widget to the frame
txt_input = scrolledtext.ScrolledText(frame1, wrap=tk.WORD)
txt_input.pack(expand=True, fill='both')

# Menu setup
menu = Menu(root)
root.config(menu=menu)

# File menu
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: notebook.add(ttk.Frame(), text=f"Untitled {len(notebook.tabs()) + 1}"))  # Adds a new tab
file_menu.add_command(label="Open", command=None)  # Placeholder function
file_menu.add_command(label="Save", command=None)  # Placeholder function
file_menu.add_command(label="Exit", command=root.destroy)

# Edit menu for undo, redo, cut, copy, paste
edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=None)  # Placeholder function
edit_menu.add_command(label="Redo", command=None)  # Placeholder function
edit_menu.add_command(label="Cut", command=None)  # Placeholder function
edit_menu.add_command(label="Copy", command=None)  # Placeholder function
edit_menu.add_command(label="Paste", command=None)  # Placeholder function

# Execute menu to run DuckyScript
execute_menu = Menu(menu)
menu.add_cascade(label="Execute", menu=execute_menu)
execute_menu.add_command(label="Run DuckyScript", command=None)  # Placeholder function

# Search menu (can be expanded upon)
search_menu = Menu(menu)
menu.add_cascade(label="Search", menu=search_menu)
search_menu.add_command(label="Find...", command=None)  # Placeholder function

root.mainloop()
