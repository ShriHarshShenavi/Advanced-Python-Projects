import cv2
import os
image = cv2.imread("cat.jpg")
print(image.shape)
print(image.size)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image1 = cv2.imread("WhatsApp Image 2026-06-25 at 5.33.57 PM.jpeg",0)
cv2.imshow("image1", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("cat.jpg",image1)