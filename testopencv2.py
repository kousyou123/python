import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

cap = cv2.VideoCapture(0)
for i in range(0, 19):
    print(cap.get(i))

while(1):
    ret, frame = cap.read()
     # color = ('b', 'g', 'r')
    color = ((255,0,0), (0,255,0), (0,0,255))

    for i, col in enumerate(color):
        hist = cv2.calcHist([frame], [i], None, [256], [0, 256])
        minVal, maxVal,minPos,maxPos = cv2.minMaxLoc(hist)
        # print(minVal, maxVal,minPos,maxPos)
        histImage = np.zeros([256,256,3], np.uint8)
        for x in range(256):
            cv2.line(histImage, (x,256), (x, 256-(hist[x]/maxVal)*250), col)
        cv2.imshow("Hist{}".format(i), histImage)
    cv2.imshow("Capture", frame)
     # time.sleep(0.01)

    key = cv2.waitKey(1)
    if key & 0xff == ord('q') or key == 27:
        print(frame.shape,ret)
        break
cap.release()
cv2.destroyAllWindows()