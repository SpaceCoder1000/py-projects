import ctypes
import time
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox

# Constants
user32 = ctypes.windll.user32

# Global variables
running = False
cps = 10  # Default CPS

# Click function
def click_mouse():
    user32.mouse_event(2, 0, 0, 0, 0)  # Mouse down
    user32.mouse_event(4, 0, 0, 0, 0)  # Mouse up

# Auto-clicker function
def auto_clicker():
    global running
    while running:
        click_mouse()
        time.sleep(1 / cps)

# Start clicking
def start_clicking():
    global running
    if not running:
        running = True
        threading.Thread(target=auto_clicker, daemon=True).start()

# Stop clicking
def stop_clicking():
    global running
    running = False

# Input CPS
def input_cps():
    global cps
    cps_input = simpledialog.askstring("Input CPS", "Enter clicks per second:")
    if cps_input and cps_input.isdigit():
        cps = int(cps_input)
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Check for Esc key press
def check_for_escape():
    while True:
        if ctypes.windll.user32.GetAsyncKeyState(0x1B):  # 0x1B is the virtual key code for Esc
            stop_clicking()
            break
        time.sleep(0.1)

# Create the main window
def create_window():
    global running, cps
    window = tk.Tk()
    window.title("Auto Clicker")
    window.attributes("-topmost", True)  # Keep window on top

    # Button to start clicking
    start_button = tk.Button(window, text="Start Clicking", command=start_clicking)
    start_button.pack(pady=10)

    # Button to stop clicking
    stop_button = tk.Button(window, text="Stop Clicking", command=stop_clicking)
    stop_button.pack(pady=10)

    # Button to set CPS
    cps_button = tk.Button(window, text="Set CPS", command=input_cps)
    cps_button.pack(pady=10)

    # Button to exit
    exit_button = tk.Button(window, text="Exit", command=window.quit)
    exit_button.pack(pady=10)

    # Start thread to check for Esc key
    threading.Thread(target=check_for_escape, daemon=True).start()

    # Allow the window to be moved
    window.bind("<Button-1>", lambda event: window.lift())  # Bring window to front when clicked

    window.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_window()
