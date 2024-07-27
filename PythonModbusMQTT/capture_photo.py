import cv2
import paho.mqtt.client as mqtt
import os
from datetime import datetime

MQTT_BROKER = "192.168.1.12"
MQTT_PORT = 1883
MQTT_TOPIC_CAPTURE = "webcam/capture"
MQTT_TOPIC_PHOTO = "webcam/photo"
MQTT_TOPIC_INFO = "webcam/info"
SAVE_DIR = "captured_images"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

def capture_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(SAVE_DIR, f"{timestamp}.jpg")
        cv2.imwrite(file_path, frame)
        client.publish(MQTT_TOPIC_INFO, f"{file_path},{timestamp}")
        client.publish(MQTT_TOPIC_PHOTO, file_path)
        cap.release()
        return True
    else:
        cap.release()
        return False

def on_message(client, userdata, msg):
    if msg.topic == MQTT_TOPIC_CAPTURE:
        capture_photo()

client.on_message = on_message
client.subscribe(MQTT_TOPIC_CAPTURE)
client.loop_start()

if __name__ == '__main__':
    print("Waiting for capture command...")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()
