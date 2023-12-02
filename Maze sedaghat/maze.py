import cv2 
from maze import Maze

image = cv2.imread("background1.png")
h , w , _ = image.shape

robot = cv2.imread("robot.png")
robot_w , robot_h , _ = robot.shape


font = cv2.FONT_HERSHEY_SIMPLEX




h_block_size =  int((h-100) / int(len(Maze)/2))
w_block_size = int((w-100) / max([len(i) for i in Maze]))

block_size = min(w_block_size , h_block_size)

color = (0 , 0 ,0)


if h_block_size > w_block_size :
    start_point = [ 50 ,  int((h - (block_size * int(len(Maze)/2))) / 2) ]

else :
    start_point = [int((w - (block_size *  max([len(i) for i in Maze]))) / 2), 50 ]

robot_pos = []
robot_block = []



for row in range(len(Maze)) :
    
    for block in range(len(Maze[row])) :
        _ = int(row/2) 

        if Maze[row][block] == "--" :

            x , y = start_point[0] + block_size * (block) , start_point[1] + block_size * (int(row/2))
            robot_pos = [x + int(block_size/2) - int(robot_w/2) , y - int(block_size/2) - int(robot_h/2)] 

            robot_block = [block , _ - 1]

        if Maze[row][block] == "-" :

            x1 , y1 = start_point[0] + block_size * (block) , start_point[1] + block_size * (int(row/2))
            x2 , y2 = x1 + block_size , y1
            image = cv2.line(image, (x1 , y1), (x2 , y2 ),color , 3)

        if Maze[row][block] == "|#" :

            x1 , y1 = start_point[0] + block_size * (block) , start_point[1] + block_size * (int(row/2))
            x2 , y2 = x1  , y1 + block_size
            image = cv2.line(image, (x1 , y1), (x2 , y2 ), color , 3)

        if Maze[row][block] == "#|" :

            x1 , y1 = start_point[0] + block_size * (block+1) , start_point[1] + block_size * (int(row/2))
            x2 , y2 = x1  , y1 + block_size
            image = cv2.line(image, (x1 , y1), (x2 , y2 ), color , 3)

        if Maze[row][block] == "|#|" :

            x1 , y1 = start_point[0] + block_size * (block) , start_point[1] + block_size * (int(row/2))
            x2 , y2 = x1  , y1 + block_size
            image = cv2.line(image, (x1 , y1), (x2 , y2 ), color , 3)
            x1 , y1 = start_point[0] + block_size * (block+1) , start_point[1] + block_size * (int(row/2))
            x2 , y2 = x1  , y1 + block_size
            image = cv2.line(image, (x1 , y1), (x2 , y2 ), color , 3)

        if "#" in Maze[row][block] :
            x1 , y1 = start_point[0] + block_size * (block) , start_point[1] + block_size * (int(row/2))
            image = cv2.putText(image, f'{block} {_}', (x1 + 20 , y1 + 20) , font, 
                            0.5, color, 2, cv2.LINE_AA)

config = open("config.py" , "w")

config.write(f"W = {w} \n")
config.write(f"H = {h} \n")

config.write(f"START_POINT = {start_point} \n")
config.write(f"BLOCK_SIZE = {block_size} \n")

config.write(f"ROBOT_POS = {robot_pos} \n")
config.write(f"ROBOT_BLOCK = {robot_block}")

cv2.imwrite("Maze.png" , image)
