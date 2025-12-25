import cv2
from crowd_detection.detector import detect_people_and_heatmap

cap = cv2.VideoCapture("http://192.168.4.1:81/stream")  # webcam

if not cap.isOpened():
    print("ERROR: Webcam not accessible")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    overlay, heat, count = detect_people_and_heatmap(frame)

    cv2.putText(
        overlay,
        f"People detected: {count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        (255, 255, 255),
        2,
        cv2.LINE_AA
    )

    cv2.imshow("Crowd Density Heatmap", overlay)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
