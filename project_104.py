import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255))
cv2.putText(img,"Mercury",(110,188),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Venus",(190,258),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Earth",(280,168),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Mars",(385,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Jupiter",(516,210),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
cv2.putText(img,"Saturn",(770,128),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Uranus",(965,290),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Neptune",(1110,145),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imshow("output",img)
cv2.waitKey(0)

cv2.imwrite("Solar-system-name.jpg",img)

