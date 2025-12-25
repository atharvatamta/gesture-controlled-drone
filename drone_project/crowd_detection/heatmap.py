import cv2
import numpy as np

# Tunables (TEST MODE)
MIN_R, MAX_R = 6, 40
BLUR_KSIZE = 51
TARGET_RED = 1.5   # LOWER → heatmap clearly visible on webcam

def build_density_heatmap(frame, people_boxes):
    h, w = frame.shape[:2]
    heat = np.zeros((h, w), np.float32)

    for (x1, y1, x2, y2) in people_boxes:
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        hbox = max(1, y2 - y1)
        rpx = int(np.clip(0.25 * hbox, MIN_R, MAX_R))
        cv2.circle(heat, (cx, cy), rpx, 1.0, -1)

    heat = cv2.GaussianBlur(heat, (BLUR_KSIZE, BLUR_KSIZE), 0)
    heat = np.clip(heat / TARGET_RED, 0.0, 1.0)
    return heat

def overlay_heatmap(frame, heat, alpha_img=0.55, alpha_heat=0.45):
    heat_u8 = (heat * 255).astype(np.uint8)
    heat_color = cv2.applyColorMap(heat_u8, cv2.COLORMAP_TURBO)
    overlay = cv2.addWeighted(frame, alpha_img, heat_color, alpha_heat, 0)
    return overlay
