# bitwise operatörleri

import cv2

img = cv2.imread("picture4.jpg",0)
img1 = cv2.imread("picture5.jpg",0)

if img.shape != img1.shape:
    img1 = cv2.resize(img1, (img.shape[1], img.shape[0]))

and_bitwise = cv2.bitwise_and(img,img1)
or_bitwise = cv2.bitwise_or(img,img1)
xor_bitwise = cv2.bitwise_xor(img,img1) #veya
not_bitwise = cv2.bitwise_not(img)
not_bitwise1 = cv2.bitwise_not(img1)

cv2.imshow("orijinal image 1",img)
cv2.imshow("orginal image 2",img1)
cv2.imshow("bitwise and", and_bitwise)
cv2.imshow("bitwise or",or_bitwise)
cv2.imshow("bitwise xor",xor_bitwise)
cv2.imshow("bitwise not image 1",not_bitwise)
cv2.imshow("bitwise not image 2",not_bitwise1)

cv2.waitKey(0)
cv2.destroyAllWindows()