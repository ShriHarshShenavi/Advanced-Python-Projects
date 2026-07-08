import cv2
cap=cv2.VideoCapture(0)
ret,frame1=cap.read()
ret, frame2=cap.read()

while cap.isOpened():
    diff=cv2.absdiff(frame1,frame2)#diff bet 2 frames
    grey=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(grey,(5,5),0)
    #Apply Threshold
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    #Find Counters
    contours,_=cv2.findContours(
        thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    #Check Motion
    for cnt in contours:
        if cv2.contourArea(cnt)<1000:
            x,y,w,h=cv2.boundingRect(cnt)
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame1,"Motion Detected",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    #Show Video
    cv2.imshow('Motion Detected',frame1)
    #Update Frames
    frame1=frame2
    ret,frame2=cap.read()
    #Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()