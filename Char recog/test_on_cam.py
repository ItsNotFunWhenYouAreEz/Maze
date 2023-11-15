import cv2
from utils import approx_predict
import time
vid = cv2.VideoCapture("U.mp4")


font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (0, 0, 0)
thickness = 2


prev_frame_time = 0
new_frame_time = 0

while(True):

    ret, frame = vid.read()
    
    if ret :
        char , image = approx_predict(frame)
        image = cv2.putText(frame, char, org, font, 
                        fontScale, color, thickness, cv2.LINE_AA)
        new_frame_time = time.time()
    
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time

        fps = str(int(fps))

        cv2.putText(image, fps, (7, 200), font, 3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', image)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.05)
    else :
        break

vid.release()
cv2.destroyAllWindows()

