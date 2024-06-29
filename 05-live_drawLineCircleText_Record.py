# kameradan canlı video alma
# canlı görüntüye çizgi, daire,metin ekleme
# kameradan alınan görüntünün kayıt edilmesi

import cv2

camera = cv2.VideoCapture(0) # 0 bilgisayar kamerası , 1 harici kamera

width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)) # çerçeve genişliği
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)) # çerçeve yüksekliği
print("frame size:\t",width,"x",height)

fourcc = cv2.VideoWriter_fourcc(*'MP4V') # video formatı
# VideoWriter için codec tanımlama, four caracter code , encoding işlemi

writer = cv2.VideoWriter("record.mp4",fourcc,20,(width,height)) 
# çıkış dosyası,codec(format),FPS(saniyelik görüntü sayısı hızlı mı yavaş mı versiyonda kayıt edilsin), çerçeve boyutu

while True:
    ret,frame = camera.read() 
    # 20 milisaniyede bir kare resim çeker ve birleştirir,döngü içinde bunu alır
    # ret bloon türündedir,kamera çalışıyorsa 1 döndürür
    # ret kameranın çalışıp çalışmadığını kontrol eder 
    if not ret:
        break
    
    cv2.rectangle(frame,(100,100),(200,200),(200,200,50),2) #dikdörtgen ekleme
    # (çizilecek kare,sol üst köşesi,sağ alt köşesi,rengi,kalınlığı)
    cv2.line(frame,(100,100),(250,250),(100,50,0),2)
    # (çizilecek kare,başlangıç koordinatı,bitiş koordinatı,rengi,kalınlığı)
    cv2.circle(frame,(150,150),20,(200,10,50),1)
    # (çizilecek kare, merkezinin koordinatları,yarıçap,renk,kalınlık)
    cv2.putText(frame,"lorem epsum",(50,250),cv2.FONT_HERSHEY_COMPLEX,1,(150,150,10))
    # (yazılacak kare,metin,başlangıç koordinatı,font,kalınlığı,rengi)
    
    cv2.imshow("recording",frame) # kareyi gösterir
    writer.write(frame) # kareyi video dosyasına yazar     
    
    if cv2.waitKey(30) & 0xFF == ord("q"): # 30 milisaniyede bir çeker, ve çıkış q'ya eşit ise
        break

camera.release() # okuma başlatılan kamera serbest bırakılır
writer.release() # yazıcı serbest bırakılır 
cv2.destroyAllWindows()