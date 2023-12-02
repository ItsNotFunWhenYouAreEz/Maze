import cv2
from utils import approx_predict
import time
vid = cv2.VideoCapture(0)


font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (0, 0, 0)
thickness = 2
last10_images = [ ]

prev_frame_time = 0
new_frame_time = 0

while(True):

    ret, frame = vid.read()
    
    if ret :
        char , image = approx_predict(frame)
        image = cv2.putText(frame, char, org, font, 
                        fontScale, color, thickness, cv2.LINE_AA)
        new_frame_time = time.time()





        #cv2.putText(image, fps, (7, 200), font, 3, (0, 255, 0), 3, cv2.LINE_AA)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    else :
        break

vid.release()
cv2.destroyAllWindows()

