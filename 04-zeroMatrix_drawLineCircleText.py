# numpy sıfır matrisi ile resim oluşturma
# çizgi, daire, metin oluşturma

import cv2
import numpy as np

canvas = np.zeros((300,300,3),dtype="uint8") 
# 300x300 boyutunda, üç kanallı, bir sıfır matrisi oluşturur
print(canvas)

cv2.line(canvas,(0,0),(100,100),(100,20,50),2) #çizgi çekme
# (çizilecek resim,başlangıç koordinatları,bitiş koordinatları,renk,kalınlık)
cv2.circle(canvas,(150,100),25,(100,70,10),2)
# (çizilecek resim,dairenin merkez koordinatları,yarıçap,renk,kalınlık)
cv2.putText(canvas,"lorem epsum",(50,200),cv2.FONT_HERSHEY_COMPLEX,1,(50,100,30),1)
# (yazılacak resim,yazı,başlangıç koordinatı,font,ölçek,renk,kalınlık)

cv2.imshow("window",canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()


