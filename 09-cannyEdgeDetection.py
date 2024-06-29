# canny kenar algılama algoritması

import cv2
import numpy as np

image = cv2.imread("picture1.jpg")
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur_image = cv2.GaussianBlur(gray_image,(3,3),0)

def autoCanny(blur, sigma=0.33):
    median = np.median(blur)
    lower = int(max(0,(1.0-sigma)*median))
    upper = int(max(255,(1.0+sigma)*median))
    canny = cv2.Canny(blur,lower,upper)
    return canny

wide = cv2.Canny(blur_image,10,220)
# (işlenecek resim,alt eşik değeri, üst eşik değeri)
tight = cv2.Canny(blur_image,200,230)

auto = autoCanny(blur_image)

cv2.imshow("original gray image",blur_image)
cv2.imshow("edges",np.hstack([wide,tight,auto]))

cv2.waitKey(0)
cv2.destroyAllWindows()