import firebase_helper
import clipboard


def firebase_stream_handler(post):
    if post["event"] == "put":
        if isinstance(post["data"], list):
            list(clipboard.copy_to_clipboard(post["data"].values)[-1])
        else:
            clipboard.copy_to_clipboard(post["data"])

firebase_helper.listen_to_firebase(firebase_stream_handler)
clipboard.listen_to_clipboard(firebase_helper.send_to_firebase)
