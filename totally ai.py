#this is just a troll ai for computers
import ctypes
import time
import turtle as t

VK_LWIN = 0x5B 
VK_M = 0x4D 
VK_ALT = 0x12  
VK_F4 = 0x73   
VK_ENTER = 0x0D 

def simulate_keys():
    # Simulate Windows + M
    ctypes.windll.user32.keybd_event(VK_LWIN, 0, 0, 0)  # Press down Windows key
    ctypes.windll.user32.keybd_event(VK_M, 0, 0, 0)      # Press down M key
    ctypes.windll.user32.keybd_event(VK_M, 0, 2, 0)      # Release M key
    ctypes.windll.user32.keybd_event(VK_LWIN, 0, 2, 0)   # Release Windows key

    # Add a short delay to ensure the system processes the previous keys
    time.sleep(0.1)

    # Simulate Alt + F4
    ctypes.windll.user32.keybd_event(VK_ALT, 0, 0, 0)    # Press down Alt key
    ctypes.windll.user32.keybd_event(VK_F4, 0, 0, 0)      # Press down F4 key
    ctypes.windll.user32.keybd_event(VK_F4, 0, 2, 0)      # Release F4 key
    ctypes.windll.user32.keybd_event(VK_ALT, 0, 2, 0)     # Release Alt key

    # Add a short delay to ensure the system processes the previous keys
    time.sleep(0.1)

    # Simulate Enter key
    ctypes.windll.user32.keybd_event(VK_ENTER, 0, 0, 0)   # Press down Enter key
    ctypes.windll.user32.keybd_event(VK_ENTER, 0, 2, 0)   # Release Enter key

def display_messages():
    t.setup(width=800, height=600)
    pen = t.Turtle()
    pen.hideturtle()
    pen.speed(0)
    
    pen.write('Hello, I\'m Boby the A.I.', align="center", font=("Consolas", 24, "normal"))
    time.sleep(2)
    pen.clear()
    
    pen.write('Unfortunately, I don\'t like you', align="center", font=("Consolas", 24, "normal"))
    time.sleep(2)
    pen.clear()
    
    pen.write('So, BYE', align="center", font=("Consolas", 24, "normal"))
    time.sleep(1)
    pen.clear()
    
    t.bye()  # Close the turtle graphics window

if __name__ == "__main__":
    display_messages()
    simulate_keys()
