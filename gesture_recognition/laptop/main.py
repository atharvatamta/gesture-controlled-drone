import cv2
from gesture.gesture_detector import detect_gesture
from gesture.gesture_mapper import map_gesture_to_command
from gesture.gesture_smoother import GestureSmoother
from communication.udp_sender import send_command
from ui.draw_utils import draw_text

cap = cv2.VideoCapture(0)
smoother = GestureSmoother(window_size=5, cooldown=0.5)

current_gesture = "None"
current_command = "None"

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gesture = detect_gesture(frame)

    if gesture:
        current_gesture = gesture

    stable_gesture = smoother.update(gesture)

    if stable_gesture:
        command = map_gesture_to_command(stable_gesture)
        if command:
            current_command = command
            print("Stable Command:", command)
            send_command(command)

    draw_text(frame, current_gesture, current_command)

    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
