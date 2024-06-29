# resmi grileştirme
# piksellerin ve resimlerin ağırlıklı toplamı
# görüntü piramitleri

import cv2

img_path = "picture.jpg"
img_path1 = "picture1.jpg"

img = cv2.imread(img_path)
img1 =  cv2.imread(img_path1) 

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
# bgr'ı gri tonlamaya dönüştürür

height, width, number_of_channel = img.shape
print("color image dimensions:\t",height,"x",width,"x",number_of_channel)

height1, width1 = gray_img.shape
print("grayscale image dimensions:\t",height1,"x",width1)

cv2.imshow("gray img",gray_img)

print("pixel value at (100,100) in image 1:\t",img[100,100]) # çıktı: [172 141 2]
print("pixel value at (75,75) in image 2:\t",img1[75,75]) # çıktı: [211 208 204] 
print("sum of pixels at (100,100) in image 1 and (75,75) in image 2:\t",img[100,100] + img1[75,75]) # çıktı: [127  93 206] 

"""
ağırlıklı toplama
piksel1 = [200,100,50]
piksel2 = [100,50,210]
toplam 255i geçerse devir dönüşümü yapılır 0 dahil olduğu için 256 çıkarılır
200+100= 300 -256 = 44
100+50 = 150
50+210 = 260 -256 = 4
sum_piksel = [44,150,4]
"""

# görüntülerin boyutu aynı olmalı
if img.shape != img1.shape:
    img1 = cv2.resize(img1, (img.shape[1], img.shape[0]))

sum_img = cv2.add(img,img1) # resimleri üst üste ekler
weighted_sum_img = cv2.addWeighted(img,0.7,img1, 0.3,0) 
# (1.resim, 1.resmin yüzdesi, 2.resim, 2.resmin yüzdesi,son parametre 0'dır)

cv2.imshow("summed image",sum_img)
cv2.imshow("weighted sum image",weighted_sum_img)

# resim piramitleri
doubled_img = cv2.pyrUp(img) 
# resmin boyutunu iki kat arttırır
half_size_img = cv2.pyrDown(img) 
# resmin boyutunu iki kat azaltır

print("original image dimensions" + str(img.shape))
print("double image dimensions" + str(doubled_img.shape) )
print("halved image dimensions" + str(half_size_img))

cv2.imshow("original image",img)
cv2.imshow("doubled image",doubled_img)
cv2.imshow("halved image",half_size_img)

cv2.waitKey(0)
cv2.destroyAllWindows()