import cv2
import numpy as np



vid = cv2.VideoCapture("1.mp4")

while True :
    ret , img = vid.read()
    if ret :
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.blur(gray, (3, 3))

        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1 , 150 , param1 = 60, param2 = 50, minRadius = 1, maxRadius = 100)


        if circles is not None:
        
            circles = np.uint16(np.around(circles))
        
            for pt in circles[0, :]:
                x , y , r = pt[0], pt[1], pt[2]

                cv2.circle(img, (x, y), r , (0, 255, 0), 2)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        cv2.imshow("out", img)
    else :
        break
