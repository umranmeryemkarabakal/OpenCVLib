# resmi bölgesel çerçeveye alma
# resme filtre ekleme
# resimden kesit alma,yapıştırma,filtreleme
# resmi kopyalma: aynalama, uzatma, tekrar etme

import cv2

img_path =  "picture.jpg"

img = cv2.imread(img_path)

cv2.rectangle(img,(100,100),(200,200),(10,40,100)) 
# resme bölgesel çerçeve ekler (kullanılacak resim,çerçevenin sol alt köşesinin koordinatları(x,y),sağ üst köşenin koordinatları(x,y),çerçevenin rengi bgr)

img[:,:,0] = 150 
# tüm resme yaklaşık mavi filtre uygular
# bgr 0-mavi 1-yeşil 2-kırmızı filtre yapar
 
img[10:30,20:50,1] = 100 
# y indeksi 10'dan 30'a , x indeksi 20'den 50'ye filtre uygular 

section = img[60:70,60:70] 
# resimden kesit alır
section[:,:,0] = 150

img[90:100,90:100] = section 
# kesiti resme yapıştır -piksel koordinatları tutarlı olmalıdır-
 
img[25:45,35:75] = (200,150,0) 
# resim berirli bölgesini boyar 'bgr'

cv2.imshow("image",img)
cv2.imshow("section",section)

# kenarlık efektleri
mirroring_img = cv2.copyMakeBorder (img,100,100,150,150,cv2.BORDER_REFLECT) 
# sınır yapılacağı ve kopyalama yapılacağı için bu fonk kullanılır , (işlem yapılacak resim, üst alt sol sağ boyutları,cv2nin aynalama parametresi: sınırları tekrarla )
stretched_img = cv2.copyMakeBorder(img, 200,200,150,150,cv2.BORDER_REPLICATE) 
repeating_img = cv2.copyMakeBorder(img,200,200,100,100,cv2.BORDER_WRAP)
framed_img = cv2.copyMakeBorder(img,150,150,150,150,cv2.BORDER_CONSTANT, value = (50,20,130)) 
# constant : sabit, kenarlığa renk: son parametre yazılmazsa defalult siyah çerçeve çeker

cv2.imshow("mirrored image",mirroring_img)
cv2.imshow("stretched image",stretched_img)
cv2.imshow("repeating image",repeating_img)
cv2.imshow("framed image",framed_img)

cv2.waitKey(0)
cv2.destroyAllWindows()