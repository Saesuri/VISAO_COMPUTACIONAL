# testes aqui

import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg2 = cv2.createBackgroundSubtractorMOG2()

pTime = 0

while True:
    ret, frame = cap.read()
    flipped_frame = cv2.flip(frame, 1)

    fgmask = fgbg.apply(flipped_frame)
    fgmask2 = fgbg2.apply(flipped_frame) # com MOG 2

    hsv = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2HSV)
    blur = cv2.medianBlur(hsv ,7)

    lower_azul = np.array([100, 150, 50])
    upper_azul = np.array([130, 255, 255])
    
    lower_verde = np.array([35, 100, 100])
    upper_verde = np.array([85, 255, 255])  

    lower_vermelho2 = np.array([160, 100, 100])
    upper_vermelho2 = np.array([179, 255, 255])

    lower_vermelho = np.array([0, 100, 100])
    upper_vermelho = np.array([10, 255, 255])

    mask_r1 = cv2.inRange(blur, lower_vermelho, upper_vermelho)
    mask_r2 = cv2.inRange(blur, lower_vermelho2, upper_vermelho2)

    green_mask = cv2.inRange(blur, lower_verde, upper_verde)
    red_mask = mask_r1 + mask_r2
    blue_mask = cv2.inRange(blur, lower_azul, upper_azul)

    key = cv2.waitKey(1)
    if key == 27:
        break


    # mostrar diferença entre mog e mog 2
    # cv2.imshow('movimento', fgmask)
    # cv2.imshow('movimento', fgmask2)

    # mostrar fps

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(flipped_frame, f"FPS: {int(fps)}", (50, 50), 
    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

    # cv2.imshow("webcam", flipped_frame)
    # cv2.imshow('movimento_MOG2', fgmask2)
    # cv2.imshow('mascara verde', green_mask)
    # cv2.imshow('mascara azul', blue_mask)
    # cv2.imshow('mascara vermelha', red_mask)

    fgmask_color = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR)
    fgmask2_color = cv2.cvtColor(fgmask2, cv2.COLOR_GRAY2BGR)

    azul_x_vermelho = cv2.hconcat([blue_mask, red_mask])
    webXmask = cv2.hconcat([flipped_frame, fgmask_color])
    webXmask2 = cv2.hconcat([flipped_frame, fgmask2_color])
    cv2.imshow("webXmaska", webXmask2)
    cv2.imshow("webXmask", webXmask)


cap.release()

#  FEITO: processar um fluxo de vídeo
#  detectar movimento em uma "Zona de Interesse" definida   