import cv2

cap = cv2.VideoCapture(0)

while True:
    
    _, frame = cap.read()
    hsvColor = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    height, width, _ = frame.shape
    centerX = int(width / 2)
    centerY = int(height / 2)
    
    theColor = hsvColor[centerY , centerX]
    print(theColor)
    cv2.circle(frame, (centerX,centerY), 5, (0, 0, 255),6)

    cv2.imshow("Frame", frame)
    cv2.waitKey(1)