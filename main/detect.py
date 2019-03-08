import pytesseract as ocr
import numpy as np
import argparse
import cv2
import os

from PIL import Image

test = ocr.image_to_string(Image.open('E:/ProjectsTeste--Pycharm/PProcessamento_tcc/image/1.png'))
os.remove('E:/ProjectsTeste--Pycharm/PProcessamento_tcc/image/1.png')
print(test)


#img = cv2.imread('E:/ProjectsTeste--Pycharm/PProcessamento_tcc/image/1.png')
#cv2.imshow('img', img)

#cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('cinza', cinza)

#ret, bin = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)
#cv2.imshow('bin', bin)

#desfoque = cv2.GaussianBlur(bin, (5, 5), 0)
#cv2.imshow('des', desfoque)

#contornos, hier = cv2.findContours(desfoque, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#cv2.drawContours(img, contornos, -1, (0, 255, 0), 2)
#cv2.imshow('cont', img)


#for c in contornos:
#    perimetro = cv2.arcLength(c, True)
 #   if perimetro > 120:
  #      aprox = cv2.approxPolyDP(c, 0.03 * perimetro, True)
   #     if len(aprox) == 4:
    #        (x, y, h, w) = cv2.boundingRect(c)
     #       cv2.rectangle(img, (x, y), (x+h, y+w), (0, 255, 0), 1)
      #      roi = img[y:y + w, x:x + h]
       #     cv2.imwrite('rest/roi.jpg', (x+h, y+w))

#cv2.imshow('draw', img)



cv2.waitKey(0)
cv2.destroyAllWindows()