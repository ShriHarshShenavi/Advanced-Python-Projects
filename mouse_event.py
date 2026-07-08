import numpy as np
import cv2

#event=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)
#Mouse call back fn
img=cv2.imread('car.jpg')
def click(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY=str(x)+","+str(y)
        cv2.putText(img,strXY,(x,y),font,1,(255,255,0),2)
        cv2.imshow('img',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font= cv2.FONT_HERSHEY_SIMPLEX
        strXY=str(blue)+","+str(green)+","+str(red)
        cv2.putText(img,strXY,(x,y),font,1,(0,255,255),2)
        cv2.imshow('img',img)
cv2.imshow('img',img)
cv2.setMouseCallback('img',click)
cv2.waitKey(0)
cv2.destroyAllWindows()
