import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('1.jpg')

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(pytesseract.image_to_string(img))

height_image, width_image = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(width_image- x,height_image-y),(width_image- w,height_image - h),(0,0,255), 1)
    cv2.putText(img,b[0],(width_image- x,height_image-y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow('result', img)
cv2.waitKey(0)

