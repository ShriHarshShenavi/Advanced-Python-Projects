import cv2
import numpy as np
import tkinter as tk

root = tk.Tk()
root.withdraw()

image = cv2.imread("apple.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_red = np.array([0,120,70)]
upper_red = np.array([10,255,255])

mask = cv2.inRange(hsv, lower_red, upper_red)

result=cv2.bitwise_and(image,image,mask=mask)

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

image_height,image_width=image.shape[:2]

x_center=int((screen_width)-(image_width)/2)
y_center=int((screen_height)-(image_height)/2)

cv2.imshow("original",image)
cv2.imshow("mask",mask)
cv2.imshow("result",result)

cv2.moveWindow("original",x_center,y_center)
cv2.moveWindow("mask",x_center-450,y_center)
cv2.moveWindow("result",x_center+450,y_center)

cv2.waitKey(0)
cv2.destroyAllWindows()