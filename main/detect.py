

##############  PYTHON 3 OU SUPERIOR

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
#from matplotlib import pyplot as plt



###Está com o diretório, porque o projeto esta em outro HD

img = cv2.imread('E:/ProjectsTeste--Pycharm/PProcessamento_tcc/image/1.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




struct = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
imgTopHat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, struct)
imgBlackHat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, struct)
imgGrayPTopHat = cv2.add(img, imgTopHat)
imgGrayPBlackHat = cv2.subtract(imgGrayPTopHat, imgBlackHat)

#laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_8U, 1,0, ksize=3,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)
sobely = cv2.Sobel(img, cv2.CV_8U, 0,1, ksize=3,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)


ret, bin = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)
#imgThs = cv2.threshold(sobelx, 0,255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)

morph = cv2.getStructuringElement(cv2.MORPH_RECT,(40,13))

plateDetect = cv2.morphologyEx(ret, cv2.MORPH_CLOSE, morph)
regionPlate = plateDetect.copy()

#contor = cv2.findContours(regionPlate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#v2.drawContours(regionPlate, contor, -1, (255,255,255),18)

###-- GAUSSIAN_SMOOTH_FILTER_SIZE = (5, 5)
imgBlur = cv2.GaussianBlur(bin, (5, 5), 0)
contornos, hier = cv2.findContours(imgBlur, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contornos, -1, (0, 255, 0), 2)

cv2.imshow('Original', img)
#cv2.imshow('Desaturada', gray)
#cv2.imshow('AltoCont', imgGrayPBlackHat)
#cv2.imshow('Desfocada', imgBlur)
#cv2.imshow('bin', bin)
#cv2.imshow('cont', img)
# Com erro #cv2.imshow('l', laplacian)
im =cv2.imshow('SobelX', sobelx)
cv2.imshow('SobelY', sobely)




for c in contornos:
    perimetro = cv2.arcLength(c, True)
    if perimetro > 120:
        aprox = cv2.approxPolyDP(c, 0.03 * perimetro, True)
        if len(aprox) == 4:
            (x, y, h, w) = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x+h, y+w), (0, 255, 0), 1)
            roi = img[y:y + w, x:x + h]
            cv2.imwrite('rest/roi.jpg', (x+h, y+w))

cv2.imshow('draw', img)





#######-- Teste 02 --#########

#test = ocr.image_to_string(Image.open('E:/ProjectsTeste--Pycharm/PProcessamento_tcc/image/1.png'))
#os.remove('E:/ProjectsTeste--Pycharm/PProcessamento_tcc/image/1.png')
#print(test)





####-- Teste 03 --#####

##-- Se não tiver tesseract no PATH, incluir este metodo:
#pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
#tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

#print(pytesseract.image_to_string(Image.open('E:/ProjectsTeste--Pycharm/PProcessamento_tcc/image/1.png')))

#print(pytesseract.image_to_string('1.png'))





#####-- Teste 04 --#####

#img = cv2.imread('E:/ProjectsTeste--Pycharm/PProcessamento_tcc/image/1.png')
#print(pytesseract.image_to_string(img))
#print(pytesseract.image_to_string(Image.fromarray(img)))








cv2.waitKey(0)
cv2.destroyAllWindows()