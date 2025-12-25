GESTURE_TO_COMMAND = {
    "OPEN_PALM": "START",
    "FIST": "STOP",
    "LEFT": "LEFT",
    "RIGHT": "RIGHT",
    "UP": "UP",
    "DOWN": "DOWN"
}

def map_gesture_to_command(gesture):
    return GESTURE_TO_COMMAND.get(gesture, None)
