import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
cTime = 0
pTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLmk in results.multi_hand_landmarks:
            for id, lm in enumerate(handLmk.landmark):
                # print(id,lm )
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                # if id == 3:
                cv2.circle(img, (cx, cy), 10, (255, 60, 55), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLmk, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 80), cv2.FONT_HERSHEY_DUPLEX, 3, (230, 30, 70), 2)

    cv2.imshow("img", img)
    cv2.waitKey(1)