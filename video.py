import cv2
cap = cv2.VideoCapture(0)
#create video writer
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output1.mp4',fourcc, 20.0, (640,480))
print("camera opened:",cap.isOpened())
while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        cv2.imshow("Webcam",frame)
        out.write(frame)

        if cv2.waitKey(1)== ord('q'):
            break


cap.release()
out.release()
cv2.destroyAllWindows()
