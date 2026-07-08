import cv2

img = cv2.imread("Dog.jpg")
# Original image
original = img.copy()
drawing = False
x1 = y1 = x2 = y2 = 0
obj = None


def mouse(event, x, y, flags, param):
    global img, original, drawing, x1, y1, x2, y2, obj
    # Left button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x1, y1 = x, y

    # Dragging
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        img = original.copy()
        cv2.rectangle(img, (x1, y1), (x, y), (0, 255, 0), 2)

    # Left button released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        x2, y2 = x, y
        xmin = min(x1, x2)
        xmax = max(x1, x2)
        ymin = min(y1, y2)
        ymax = max(y1, y2)

        # Copy ROI
        obj = original[ymin:ymax, xmin:xmax].copy()
        # Remove rectangle
        img = original.copy()
        print("object Copied!")
    # Right button -> Paste
    elif event == cv2.EVENT_RBUTTONDOWN:
        if obj is not None:
            h, w = obj.shape[:2]
            # Check boundary
            if x + w <= img.shape[1] and y + h <= img.shape[0]:
                img[y : y + h, x : x + w] = obj
                # Save pasted image
                original = img.copy()
                print("Object Pasted!")


cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse)
while True:
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
