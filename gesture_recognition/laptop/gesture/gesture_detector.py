import cv2
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

def distance(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)

def detect_gesture(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if not result.multi_hand_landmarks:
        return None

    lm = result.multi_hand_landmarks[0].landmark

    wrist = lm[0]
    index_tip = lm[8]
    thumb_tip = lm[4]
    middle_tip = lm[12]

    # Palm size reference
    palm_size = distance(wrist, middle_tip)

    # --------- FIST ----------
    if distance(index_tip, thumb_tip) < 0.25 * palm_size:
        return "FIST"

    # --------- UP / DOWN ----------
    if index_tip.y < wrist.y - 0.15:
        return "UP"

    if index_tip.y > wrist.y + 0.15:
        return "DOWN"

    # --------- LEFT / RIGHT ----------
    if index_tip.x < wrist.x - 0.15:
        return "LEFT"

    if index_tip.x > wrist.x + 0.15:
        return "RIGHT"

    return "OPEN_PALM"

