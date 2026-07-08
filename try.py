import cv2

image = cv2.imread("cat.jpg")
edge=cv2.Canny(image,100,200)
cv2.imshow("edge",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
image1=cv2.imread("cat.jpg")