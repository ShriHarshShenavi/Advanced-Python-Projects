import cv2
#load haar cascade face detection model
face_cascade=cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
image=cv2.imread("./face.jpg")

#check if image is loaded
if image is None:
    print("Image Not Found")
    exit()

#detect faces
faces=face_cascade.detectMultiScale(
    image,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
)
#print number of faces
print("number of faces:",len(faces))

#draw rectangel arouns each face
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("face detection",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
