# morfolojik işlemler
# dilation: beyaz bölgeyi arttırır nesenin kırık kesik parçalarını birleştirir
# erosion: beyaz bölgeleri küçültür, genellikle gürültüyü veya detayları azaltmak için kullanılır.
# opening: erosion üzerine dilation uygulama 
# closeing: dilation üzerine erotion uygulama
# gradyan: dilation uygulanmış resimden erosion uygulanmış resimi çıkarma
# tophat: orijinal resimden erosion uygulanmış resmi çıkarma
# blackhat: closing ile orijinal resmin arasındaki farktır

import cv2
import numpy as np

img_path = "picture2.jpg"

img = cv2.imread(img_path)

kernel = np.ones((5,5),np.uint8) 

cv2.imshow("original image",img)

dilation = cv2.dilate(img,kernel,iterations=1) 
# (kaynak,kernel,iterasyon)
dilation1 = cv2.dilate(img,kernel,iterations=2)


cv2.imshow("dilation (iteration=1)",dilation)
cv2.imshow("dilation (iteration=2)",dilation1)

erosion = cv2.erode(img,kernel,iterations=1) 
# (kaynak,çekirdek), erozyon  gürültü gidermede kullanılır genelde önce erosion sonra dilation uygulanır
erosion1 = cv2.erode(img,kernel,iterations=2)
erosion_then_dilation = cv2.dilate(erosion,kernel,iterations=1)

cv2.imshow("erosion (iterations=1)",erosion)
cv2.imshow("erosion (iterations=2)",erosion1)
cv2.imshow("erosion followed by dilation",erosion_then_dilation)

opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("gradient",gradient)
cv2.imshow("top hat",tophat)
cv2.imshow("black hat",blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()