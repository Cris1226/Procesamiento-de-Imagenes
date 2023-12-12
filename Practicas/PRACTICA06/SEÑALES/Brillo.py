import cv2
slider_max = 100
title_window = 'Brillo'
def on_trackbar(val):
  dst = src1 + val/255
  cv2.imshow(title_window, dst)
src1 = cv2.imread("NBA.jpg")/255
try:
  cv2.namedWindow(title_window)
  trackbar_name = f"Brilo {slider_max}"
  cv2.createTrackbar(trackbar_name, title_window, 0, slider_max, on_trackbar)
  on_trackbar(0)
  while True:
       key = cv2.waitKey(1)
       if key != -1:
         break
  cv2.destroyAllWindows()
except:
  cv2.destroyAllWindows()