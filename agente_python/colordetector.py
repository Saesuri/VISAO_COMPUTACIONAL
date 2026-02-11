import cv2
from util import get_limits
from PIL import Image

w = 800
h = 600

cap = cv2.VideoCapture(0)

red = [0, 0, 255]
orange = [255,165,0]
yellow = [255, 255, 0]
green = [0, 255, 0]
blue = [255, 0, 0]
purple = [128, 0, 128]
pink = [255, 20, 147]

while True:
    ret, frame = cap.read()
    hf_frame = cv2.flip(frame, 1)
    resized_frame = cv2.resize(hf_frame, (w, h))

    hsv_image = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2HSV)
    
    lower_limit, upper_limit = get_limits(color=red)


    colors = {
        "yellow": yellow,
        "red": red,
        "green": green,
        "blue": blue
    }

    counts = {}  

    for name, value in colors.items():
        lower_limit, upper_limit = get_limits(color=value)

        mask = cv2.inRange(hsv_image, lower_limit, upper_limit)

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        count = 0

        for c in contours:
            area = cv2.contourArea(c)
            if area > 200:
                count += 1

                x, y, wbox, hbox = cv2.boundingRect(c)

                cv2.rectangle(
                    resized_frame,
                    (x, y),
                    (x+wbox, y+hbox),
                    (0, 255, 0),
                    2
                )

        counts[name] = count

    print("Objetos detectados:", count)


    cv2.imshow('webcam', resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()   
cv2.destroyAllWindows()