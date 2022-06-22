import cv2

image=cv2.imread("Watermark.jpg",0)

x=image.shape[1]
y=image.shape[0]

xkali=x*2
ykali=y*2
dimensi=(xkali,ykali)
resize=cv2.resize(image,dimensi)

cv2.imshow("Original",image)
print("Ukuran asli",image.shape)
cv2.waitKey(0)
cv2.imshow("Resize",resize)
print("Ukuran ubah",resize.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()