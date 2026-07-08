import cv2

image = cv2.imread("cat.jpg")
resize=cv2.resize(image,(300,300))
cv2.imshow("Resize", resize)
cv2.waitKey(0)

rotate=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotate", rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()

flip=cv2.flip(image,1)
cv2.imshow("Flip", flip)
cv2.waitKey(0)

crop=image[100:400,100:400]
cv2.imshow("Crop", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

blur=cv2.GaussianBlur(image,(9,9),8)
cv2.imshow("Blur", blur)
cv2.waitKey(0)
