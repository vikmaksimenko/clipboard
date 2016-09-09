import pyperclip


def listen_to_clipboard(handler):
    old_val = ""
    while True:
        new_val = pyperclip.paste()
        if old_val != new_val and new_val != '':
            print("===== Copied to clipboard '%s'" % new_val)
            handler(new_val)
            old_val = new_val


def copy_to_clipboard(val):
    current_clipboard = pyperclip.paste()
    if isinstance(val, str) and val != current_clipboard:
        print("===== Pasting to clipboard '%s'" % val)
        pyperclip.copy(val)
