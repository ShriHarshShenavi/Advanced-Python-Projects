import cv2
import datetime
#how to show date and time on live video
cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#webcam current width
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 3000)#frame width
cap.set(4, 700)#frame height

print(cap.get(3))
print(cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX #chooses the font for writing text on video

        #show text height and width
        text = 'Width: ' + str(int(cap.get(3))) + ' Height: ' + str(int(cap.get(4)))
        date_time = str(datetime.datetime.now()) #show current date and time

        # Display date and time
        frame = cv2.putText(frame, date_time, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        # Display width and height
        frame = cv2.putText(frame, text, (10, 100), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()