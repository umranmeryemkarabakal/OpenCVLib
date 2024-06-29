# tresholding ,eşik ayarlama 
# simple tresholding
# adaptive thresholding
# otsu thresholding

import cv2

img_path = "picture3.jpg"
img = cv2.imread(img_path,0) #gri tonlamalı görüntü
blur_img = cv2.blur(img,(3,3))

cv2.imshow("original image",img)

ret,thresh_binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY) 
#eşik değer:127 ,127nin altında kalanlar 0'a üstündekiler 255'e çevrilir .ilk çıktı kullanılan eşik, ikinci çıktı görüntüdür
ret,thresh_binary_inv = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh_trunc = cv2.threshold(img,277,255,cv2.THRESH_TRUNC)
ret,thresh_tozero = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh_tozero_inv = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("simple thresholding -binary",thresh_binary)
cv2.imshow("simple thresholding - binary inverse",thresh_tozero_inv)
cv2.imshow("simple thresholding -truncate",thresh_trunc)
cv2.imshow("simple thresholding -to zero",thresh_tozero)
cv2.imshow("simple thresholding -to zero inverse",thresh_tozero_inv)

thresh_adaptive_mean = cv2.adaptiveThreshold(blur_img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2) #mean, ortalaması alnır .(11,2) küçük bölge berirler
thresh_adaptive_gaussian = cv2.adaptiveThreshold(blur_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)#gaussian , ağırlıklı ortalama alnır

cv2.imshow("adaptive thresholding -mean",thresh_adaptive_mean)
cv2.imshow("adaptive thresholding -gaussian",thresh_adaptive_gaussian)

ret,thresh_otsu = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
#parametre max min verilir, eşik değerler otomatik verilir

cv2.imshow("otsu's thresholding",thresh_otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()