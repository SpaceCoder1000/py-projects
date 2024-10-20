import ctypes
import time
from pynput import keyboard

# Define virtual key codes for 'W', 'A', 'S', 'D'
VK_W = 0x57  # W key
VK_A = 0x41  # A key
VK_S = 0x53  # S key
VK_D = 0x44  # D key

# Load the user32 DLL
user32 = ctypes.windll.user32

# State flags for each key
key_states = {
    'w': False,
    'a': False,
    's': False,
    'd': False
}

def press_key(vk_code):
    """Simulates a key press."""
    user32.keybd_event(vk_code, 0, 0, 0)  # Key down

def release_key(vk_code):
    """Simulates a key release."""
    user32.keybd_event(vk_code, 0, 2, 0)  # Key up

def update_key_state(direction, pressed):
    """Updates the key state and manages key presses."""
    if direction == 'w':
        if pressed and not key_states['w']:
            key_states['w'] = True
            press_key(VK_W)
        elif not pressed and key_states['w']:
            key_states['w'] = False
            release_key(VK_W)

    elif direction == 's':
        if pressed and not key_states['s']:
            key_states['s'] = True
            press_key(VK_S)
        elif not pressed and key_states['s']:
            key_states['s'] = False
            release_key(VK_S)

    elif direction == 'a':
        if pressed and not key_states['a']:
            key_states['a'] = True
            press_key(VK_A)
        elif not pressed and key_states['a']:
            key_states['a'] = False
            release_key(VK_A)

    elif direction == 'd':
        if pressed and not key_states['d']:
            key_states['d'] = True
            press_key(VK_D)
        elif not pressed and key_states['d']:
            key_states['d'] = False
            release_key(VK_D)

def on_press(key):
    """Executes when a key is pressed."""
    try:
        if key == keyboard.Key.up:
            update_key_state('w', True)
        elif key == keyboard.Key.down:
            update_key_state('s', True)
        elif key == keyboard.Key.left:
            update_key_state('a', True)
        elif key == keyboard.Key.right:
            update_key_state('d', True)
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    """Executes when a key is released."""
    if key == keyboard.Key.up:
        update_key_state('w', False)
    elif key == keyboard.Key.down:
        update_key_state('s', False)
    elif key == keyboard.Key.left:
        update_key_state('a', False)
    elif key == keyboard.Key.right:
        update_key_state('d', False)
    # Stop listener when Escape key is pressed
    if key == keyboard.Key.esc:
        release_key(VK_W)
        release_key(VK_A)
        release_key(VK_S)
        release_key(VK_D)
        return False

def main():
    """Main function to start the key listener."""
    print("Listening for arrow keys to simulate holding WASD keys in Minecraft...")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
