import cv2
import numpy as np
import requests

API_URL = "http://localhost:5105/api/eventos"

cap = cv2.VideoCapture(0)
bg = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=16,
    detectShadows=True
)

red_detected_before = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    fg_mask =  bg.apply(frame)

    kernel = np.ones((5,5), np.uint8)
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)

    contours, _ = cv2.findContours(
        fg_mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for c in contours:
        if cv2.contourArea(c) < 500:
            continue

        x, y, w, h = cv2.boundingRect(c)
        roi = frame[y:y+h, x:x+w]

        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        lower_red = np.array([0,120,70])
        upper_red = np.array([10,255,255])

        color_mask = cv2.inRange(hsv, lower_red, upper_red)

        red_detected_now = False


        if cv2.countNonZero(color_mask) > 200:
            red_detected_now = True
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if red_detected_now and not red_detected_before:
        requests.post(API_URL, json={"cor": "vermelho",
                                     "cameraId": "CAM_VICTOR.IA"
                                     })
    red_detected_before = red_detected_now

    fg_mask_bgr = cv2.cvtColor(fg_mask, cv2.COLOR_GRAY2BGR)
    cv2.imshow("test", frame)
    # criar duocolor com cv2.hconcat([])

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()