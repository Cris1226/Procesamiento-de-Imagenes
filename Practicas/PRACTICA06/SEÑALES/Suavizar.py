import cv2
from scipy import signal
import numpy as np
slider_max = 30
title_window = 'Suavizado'
def on_trackbar(val):
  kernel = np.ones((val+3,val+3))/((val+3)**2)
  out = signal.convolve2d(src1, kernel, mode= "same")
  cv2.imshow(title_window, out)
  
src1 = cv2.imread("NBA.jpg", 0)/255
print(src1.shape)


cv2.namedWindow(title_window)
trackbar_name = f"Smooth {slider_max}"
cv2.createTrackbar(trackbar_name, title_window, 0, slider_max, on_trackbar)
on_trackbar(0)
while True:
      key = cv2.waitKey(1)
      if key != -1:
        break
cv2.destroyAllWindows()





