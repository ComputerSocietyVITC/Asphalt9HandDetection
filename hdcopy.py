import cv2
from cvzone.HandTrackingModule import HandDetector
import keyboard, time
import math
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
t = 0.2
while True:
    img = cap.read()[1]
    hands = detector.findHands(img, draw=False)
    
    if len(hands) == 2:
        hand1 = hands[0]
        fingers1 = detector.fingersUp(hand1)
        hand2 = hands[1]
        fingers2 = detector.fingersUp(hand2)
        
        h1 = hand1['center']
        h2 = hand2['center']
        
        if h1[0] < h2[0]:
            right = h1
            left = h2
            rf = fingers1
            lf = fingers2
        else:
            right = h2
            left = h1
            rf = fingers2
            lf = fingers1
        
        s = math.atan((right[1] - left[1]) / (right[0] - left[0])) if (right[0] - left[0]) != 0 else 0
        if s < -0.02: 
            keyboard.press('right')
            time.sleep(abs(s*t))
            keyboard.release('right')
        elif s > 0.02:
            keyboard.press('left')
            time.sleep(abs(s*t))
            keyboard.release('left')
        
        if rf == [0, 0, 0, 0, 0]:
            keyboard.press('space')
            time.sleep(0.05)
            keyboard.release('space')
        
        if lf == [0, 0, 0, 0, 0]:
            keyboard.press('down')
            time.sleep(0.05)
            keyboard.release('down')
