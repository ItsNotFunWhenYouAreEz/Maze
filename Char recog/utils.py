import cv2 
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 255, 255)
thickness = 2


def cut_borders(img) :




    return img



def detect_object( img , x_step = 10, y_step = 1 ) :

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50 , 200 )

    w , h  = edges.shape

    x1 = w
    x2 = 0
    y1 = h
    y2 = 0 

    for x in range(0 , w , x_step) :

        for y in range(0 , h , y_step) :

            value = edges[x , y]

            if value == 255 : 

                if x1 > x :
                    x1 = x
                if x2 < x :
                    x2 = x
                if y1 > y :
                    y1 = y
                if y2 < y :
                    y2 = y



    object_detected = gray[x1-30:x2+30 ,y1-20:y2+20] 
    return object_detected



def convert_to_black_and_white(img , threshold) :

    return  255*np.uint8(img > threshold)  

def check_middle(img , x , y , x2 , y2 ) :

    #image = cv2.rectangle(img, (x , y), (x2 , y2), 0, thickness)
    #cv2.imshow("out" , image)
    #cv2.waitKey(0)

    for i in range(x , x2 , 2) :
        for j in range(y , y2 , 2) :
            
            if img[j , i] == 0 :

                return True

    return False



def approx_predict(img , threshold = 100 ):



    for i in range(threshold ,250 , 50) :

        bl = convert_to_black_and_white(img , threshold)

        bl = detect_object(bl )
        
        h , w = bl.shape



        contours, _ = cv2.findContours(bl, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        approx = 0
        middle_w , middle_h = int(w/32) , int(h/32)
        middle = check_middle(bl , int(w/2)-middle_w , int(h/2)-middle_h , int(w/2)+middle_w , int(h/2)+middle_h)

        for contour in contours:
            a = cv2.approxPolyDP(contour, 0.009 * cv2.arcLength(contour, False), True) 

            cv2.drawContours(bl, [a], 0, (0), 3)


            if approx < len(a) :
                approx = len(a)    
            print(approx)

        if middle :
            if 10 <= approx <= 14 :    
                return "H" , bl
            
            elif 15 <= approx <= 25 :
                return "S" , bl

        elif 8 <= approx <= 15 :
            return "U" , bl




    return "None" , bl

if __name__ == "__main__" :

    img = cv2.imread("9293.jpg")

    x , i = approx_predict(img)

    print(x)

    cv2.imshow("bl" , i)
    cv2.waitKey(0)


