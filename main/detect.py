try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

import cv2






#####-- Teste 04 --#####

img = cv2.imread('E:/ProjectsTeste--Pycharm/PProcessamento_tcc/image/1.png')
print(pytesseract.image_to_string(img))

print(pytesseract.image_to_string(Image.fromarray(img)))
#





#####-- Teste 03 --#####

##-- Se não tiver tesseract no PATH, incluir este metodo:
#pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
#tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

#print(pytesseract.image_to_string(Image.open('E:/ProjectsTeste--Pycharm/PProcessamento_tcc/image/1.png')))

#print(pytesseract.image_to_string('1.png'))





#######-- Teste 02 --#########

#test = ocr.image_to_string(Image.open('E:/ProjectsTeste--Pycharm/PProcessamento_tcc/image/1.png'))
#os.remove('E:/ProjectsTeste--Pycharm/PProcessamento_tcc/image/1.png')
#print(test)





#####-- Teste 01 --#####

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