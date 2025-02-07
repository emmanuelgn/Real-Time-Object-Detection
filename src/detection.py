import cv2
import numpy as np

# Carregar modelo YOLO
def load_yolo():
    net = cv2.dnn.readNet("models/yolov3.weights", "data/yolov3.cfg")
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    
    with open("data/coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    
    return net, output_layers, classes

# Função para detecção de objetos
def detect_objects(frame, net, output_layers):
    height, width, _ = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)
    return outputs, width, height
