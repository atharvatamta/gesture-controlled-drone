from ultralytics import YOLO

MODEL_PATH = "visdrone_person.pt"

_model = YOLO(MODEL_PATH)

def get_model():
    return _model
