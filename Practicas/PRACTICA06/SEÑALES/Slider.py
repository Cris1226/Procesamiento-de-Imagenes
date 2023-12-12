import cv2
import numpy as np
from scipy import signal

slider_max = 5
title_window = 'Slider'
def on_trackbar(val):
    if val > 2:
        dst = src2 + val/255
        cv2.imshow(title_window, dst)
    elif val == 1:
        blur = cv2.blur(src2, (7,7))
        mask = src2 - blur
        unsharp_image = mask + src2
        cv2.imshow(title_window, unsharp_image)

    elif val == 0:   
       A = 0
       kernel = np.array([[-1,-1,-1], [-1,A+8,-1], [-1,-1,-1]])
       out = signal.convolve2d(src2, kernel, mode= "same")
       cv2.imshow(title_window, out)
    
src1 = cv2.imread("NBA.jpg")[..., ::-1]/255
src2 = cv2.imread("NBA.jpg", 0)/255
src3 = cv2.imread("NBA.jpg")/255

cv2.namedWindow(title_window)
trackbar_name = f"??? {slider_max}"
cv2.createTrackbar(trackbar_name, title_window, 0, slider_max, on_trackbar)
on_trackbar(0)
while True:
    key = cv2.waitKey(1)
    if key != -1:
        break
cv2.destroyAllWindows()
