# filtreleme işlemleri
# mean/average filter 
# median filter
# gaussian filter 

import cv2

img_path = "picture2.jpg"
img = cv2.imread(img_path)

cv2.imshow("noisy imgage",img)

meanFilter = cv2.blur(img,(3,3)) 
# (kaynak resim, kernel(şablon) boyutları ,uygulanacak filtre)
meanFilter1 = cv2.blur(img,(5,5))

cv2.imshow("mean filtered (3x3)",meanFilter)
cv2.imshow("mean filtered (5x5)",meanFilter1)

medianFilter = cv2.medianBlur(img,3) 
# (kaynak resim,şablon boyutları)
medianFilter1 = cv2.medianBlur(img,5)

cv2.imshow("median filtered (3x3)",medianFilter)
cv2.imshow("median filtered (5x5)",medianFilter1)

gaussianFilter = cv2.GaussianBlur(img,(3,3),0)
# (kaynak resim, şablon, sigamX: 0 değişkeni)
gaussianFilter1 = cv2.GaussianBlur(img,(5,5),0)

cv2.imshow("gaussian filtered (3x3)",gaussianFilter)
cv2.imshow("mean filtered (5x5)",gaussianFilter1)

cv2.waitKey(0)
cv2.destroyAllWindows()
