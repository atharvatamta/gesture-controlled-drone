from crowd_detection.model import get_model
from crowd_detection.heatmap import build_density_heatmap, overlay_heatmap

# GLOBAL STATE (for smoothing)
prev_heat = None
prev_count = 0

def detect_people_and_heatmap(frame, conf=0.15):
    global prev_heat, prev_count

    model = get_model()
    results = model(frame, conf=conf, verbose=False)
    r = results[0]

    names = r.names
    people_boxes = []

    for b in r.boxes:
        cls_id = int(b.cls[0])
        label = names[cls_id].lower().strip()
        if label == "person":
            x1, y1, x2, y2 = map(int, b.xyxy[0])
            people_boxes.append((x1, y1, x2, y2))

    # Raw count
    raw_count = len(people_boxes)

    # Smooth count
    count = int(0.6 * prev_count + 0.4 * raw_count)
    prev_count = count

    # Heatmap
    heat = build_density_heatmap(frame, people_boxes)

    # Temporal smoothing (removes flicker)
    if prev_heat is None:
        smooth_heat = heat
    else:
        smooth_heat = 0.7 * prev_heat + 0.3 * heat

    prev_heat = smooth_heat

    overlay = overlay_heatmap(frame, smooth_heat)

    return overlay, smooth_heat, count
