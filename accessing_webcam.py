import cv2
cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()

    #gray=cv2.cvtcolor(frame,cv2.COLOR_BGR2GRAY
    cv2.imshow("frame",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    elif key==ord('s'):
        cv2.imwrite("frame1.jpg",frame)
        print("image saved")
cap.release()
cv2.destroyAllWindows()
