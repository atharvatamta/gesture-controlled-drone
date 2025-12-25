import time
from collections import deque

class GestureSmoother:
    def __init__(self, window_size=5, cooldown=0.5):
        self.window_size = window_size
        self.gesture_window = deque(maxlen=window_size)
        self.last_command_time = 0
        self.cooldown = cooldown

    def update(self, gesture):
        current_time = time.time()
        self.gesture_window.append(gesture)

        # Check if all gestures in window are same
        if len(self.gesture_window) == self.window_size:
            if len(set(self.gesture_window)) == 1:
                if current_time - self.last_command_time > self.cooldown:
                    self.last_command_time = current_time
                    return gesture

        return None
