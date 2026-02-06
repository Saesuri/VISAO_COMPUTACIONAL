# testes aqui

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret, frame = cap.read()
    flipped_frame = cv2.flip(frame, 1)

    fgmask = fgbg.apply(flipped_frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

    cv2.imshow('webcam', fgmask)

cap.release()

#  FEITO: processar um fluxo de vídeo
#  detectar movimento em uma "Zona de Interesse" definida   