# resim açma,görüntüleme,yazdırma 
# resmin matris karşılığı
# resmin fiziksel özellikleri

import cv2

img_path = "picture.jpg"

img = cv2.imread(img_path) 
# imread fonksiyonu resmi alır numpy dizisine dönüştürür
# picture = cv2.imread("picture.png",0) 
# 0 parametresi verilirse siyah-beyaz görüntü çıkar kanalları sıfırlar tek bir kanaldan görüntü verir

print("image matris:\n",img) 
# her bir pikselin matris görünümünü bastırır

print("total pixel count:\t",img.size) 
# resmin toplam pixel sayısı , çıktı:248517
print("data type:\t",img.dtype) 
# hangi veri tipini kullandığını bastırır , çıktı:uint8 her bir piksel için 8 bit kullanılmıştır
print("image dimensions (height, width,channels):\t",img.shape) 
# genişlik,yükseklik,kanal sayısını bastırır , çıktı:(159,512,3) , size = 159*512*3
print("pixel value at (230,80) 'bgr':\t",img[(230,80)]) 
# resmin sol köşesi baz alınarak 230 piksel aşağı 80 piksel sağa gidildiğindeki piksel değerlerini bastırır , çıktı: 41,92,248

cv2.imshow("original image",img) 
# original image, pencereye yazılacak isimdir, resmi göstermek için imshow fonksiyonu kullanılır

img[50,30] = [255,255,255] # (50,30) pikseli bgr değerine eşitler

for i in range(500):
    if i < img.shape[1]: # resmin genişliğini aşmamalı
        img[70,i] = [255,255,255]

for i in range(80,180):
    for j in range(80,130):
        if i < img.shape[0] and j < img.shape[1]: # resmin yüksekliğini ve genişliğini aşmamalı
            img[i,j] = [255,255,255]


cv2.imshow("modified image",img)
cv2.imwrite("new_picture.png",img) # yeni oluşturulan resmi kaydeder

cv2.waitKey(0) # pencere açıldığında herhangi bir tuşa basılmasını bekler
cv2.destroyAllWindows() # tüm pencereleri kapatır