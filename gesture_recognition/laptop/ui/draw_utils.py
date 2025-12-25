import cv2

def draw_text(frame, gesture, command):
    cv2.putText(frame, f"Detected: {gesture}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(frame, f"Command: {command}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
