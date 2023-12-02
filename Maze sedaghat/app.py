import pygame 
import time
import cv2 as cv
import threading


def next_block(walls) :

    global current_block , blocks , past_block , count ,angel
    

  
    if  tuple(current_block) in blocks:
        blocks[tuple(current_block)]["Visited"] = True
        blocks[tuple(current_block)]["walls"] = walls

    else :
        blocks[tuple(current_block)] = {"Visited" : True , "Past block" : past_block , "walls" : walls}

    past_block = current_block.copy()

    if walls["UP"] and (current_block[0] , current_block[1]+1) not in blocks :
        blocks[(current_block[0] , current_block[1]+1)] = {"Visited" : False , "Past block" : past_block , "walls" : { }}
 
    if walls["RIGHT"] and (current_block[0]+1 , current_block[1]) not in blocks:
        blocks[(current_block[0]+1 , current_block[1])] = {"Visited" : False , "Past block" : past_block , "walls" : { }} 
    
    if walls["LEFT"] and (current_block[0]-1 , current_block[1]) not in blocks:
       blocks[(current_block[0]-1 , current_block[1])] = {"Visited" : False , "Past block" : past_block , "walls" : { }}
    
    if walls["DOWN"] and (current_block[0] , current_block[1]-1) not in blocks:
        blocks[(current_block[0] , current_block[1]-1)] = {"Visited" : False , "Past block" : past_block , "walls" : { }}
         
    if check(walls) :
        go_back()
        return   



    if walls["UP"] and not blocks[(current_block[0] , current_block[1]+1)]["Visited"] :
        current_block[1] += 1 
        angel = 0
    elif walls["RIGHT"] and not blocks[(current_block[0]+1 , current_block[1])]["Visited"]:
        current_block[0] += 1 
        angel = 270 
    elif walls["LEFT"] and not blocks[(current_block[0]-1 , current_block[1])]["Visited"]:
        current_block[0] -= 1
        angel = 90 
    elif walls["DOWN"] and not blocks[(current_block[0] , current_block[1]-1)]["Visited"]:
        current_block[1] -= 1
        angel = 180
    count += 1

def go_back() :
    global current_block , past_block , count , complete , angel
    print("Going back")

    while True   :
        current_block = blocks[tuple(current_block)]["Past block"]
        
        walls = blocks[tuple(past_block)]["walls"]

        past_block = current_block

        count += 1

        if walls["UP"] and (current_block[0] , current_block[1]+1) in blocks:
            if not blocks[(current_block[0] , current_block[1]+1)]["Visited"] :
                current_block = [current_block[0] , current_block[1]+1]
                angel = 0 
                break

        elif walls["RIGHT"] and (current_block[0]+1 , current_block[1]) in blocks:
            if not blocks[(current_block[0]+1 , current_block[1])]["Visited"] :
                current_block = [current_block[0]+1 , current_block[1]]
                angel = 270
                break
        elif walls["LEFT"] and (current_block[0]-1 , current_block[1]) in blocks:
            if not blocks[(current_block[0]-1 , current_block[1])]["Visited"] :
                current_block = [current_block[0]-1 , current_block[1]]
                angel = 90 
                break

        elif walls["DOWN"] and (current_block[0] , current_block[1]-1) in blocks:
            if not blocks[(current_block[0] , current_block[1]-1)]["Visited"] :
                current_block = [current_block[0] , current_block[1]-1]
                angel = 180
                break

        print(current_block)
        if current_block == [0 , 0] :
            complete = True
            print("END")
            break

    blocks[tuple(current_block)] = {"Visited" : True , "Past block" : past_block , "walls" : walls}

def check(walls):
    try :
        if (walls["UP"] and  blocks[(current_block[0] , current_block[1]+1)]["Visited"]or not walls["UP"]) and \
        (walls["DOWN"] and blocks[(current_block[0] , current_block[1]-1)]["Visited"] or not walls["DOWN"]) and \
        (walls["RIGHT"] and blocks[(current_block[0]+1 , current_block[1])]["Visited"] or not walls["RIGHT"]) and \
        (walls["LEFT"] and blocks[(current_block[0]-1 , current_block[1])]["Visited"] or not walls["LEFT"]) :
            return True
    except :
        return False
    return False

def victeam() :
    pass

def update_screen(image , start_time) : 

    screen.fill((255 , 255 ,255))
    screen.blit(image , (0 , 0))

    if start_time :
        TIME = font.render(f'{round(time.time() - start_time , 1)}', True, (0, 0, 0))
        screen.blit(TIME , (100 , 29) )
        
        try : 
            maze = pygame.image.load(maze_file)
            screen.blit(maze , (60 , 90))

        except :
            pass
    pygame.display.update()

def colide(pos , object) :
    return True if object[0][0] <= pos[0] and pos[0] <= object[1][0] and object[0][1] <= pos[1] and  pos[1] <= object[1][1] else False 

def clicked(pos) :
    global page , start_time
    if page == 0 and colide(pos , start_button) :
        page = 1
        print("Starting")
        start_time = time.time()
    
    if page == 1 and colide(pos , finish_button) :
        print("Finish")
        print(f"elapsed time : {round(time.time() - start_time , 1 )}")
        start_time = time.time()

    if page == 1 and colide(pos , restart_buttton) :
        print("Restart")
        start_time = time.time()

def victim_detected(victim) : 
    
    if victim == "H" :
        screen.blit(vitcims["H"] , (0 , 0))

    if victim == "S" :
        screen.blit(vitcims["S"] , (0 , 0))

    if victim == "U" :
        screen.blit(vitcims["U"] , (0 , 0))
        
    if victim == "RED" :
        screen.blit(vitcims["RED"] , (0 , 0))

    if victim == "GREEN" :
        screen.blit(vitcims["GREEN"] , (0 , 0))
    
    if victim == "YELLOW" :
        screen.blit(vitcims["YELLOW"] , (0 , 0))

    pygame.display.update()
    time.sleep(5)

def draw_maze(block_walls , current_block) :
 
    global maze_config , maze_file , maze_write

    

    img = cv.imread(maze_file)
    while True :
        x , y = (current_block[0] * maze_config["Block Size"]) + maze_config["Position"][0] ,  (-current_block[1]) * maze_config["Block Size"] + maze_config["Position"][0]

        if x > 0 and y > 0 :
            break
        
        # increas maze size from top and left side


    print(x , y)
    if not block_walls["UP"] :
        cv.line(img, (x , y),
                     (x + maze_config["Block Size"] ,y ) , maze_config["Color"] , 1)
    
    if not block_walls["DOWN"] :
         cv.line(img, (x ,y + maze_config["Block Size"]),
                     (x + maze_config["Block Size"] , y + maze_config["Block Size"] ) , maze_config["Color"] , 1)
         
    
    if not block_walls["RIGHT"] :
        cv.line(img, (x + maze_config["Block Size"] ,y),
                     (x + maze_config["Block Size"] , y + maze_config["Block Size"] ) , maze_config["Color"] , 1)
        

    if not block_walls["LEFT"] :
        cv.line(img, (x ,y),
                     (x ,y+ maze_config["Block Size"] ) , maze_config["Color"] , 1)




    cv.imwrite(maze_write , img)

    if maze_file == "maze.png" :
        maze_file = "maze2.png" 
        maze_write = "maze.png"

    else :
        maze_file = "maze.png" 
        maze_write = "maze2.png"

def maze() :
    global walls , current_block , past_block

    while True :

        print(current_block)
        
        walls = list(map(int , input("UP DOWN RIGHT LEFT \n").split()))
        walls = {"UP" : walls[0] , "DOWN" : walls[1] , "RIGHT" : walls[2] , "LEFT" : walls[3]}

        draw_maze(walls , current_block)

        next_block(walls)

        if complete :
            print("Finish")

pygame.init()
pygame.font.init() 
m
font = pygame.font.SysFont('Myriad Arabic', 30 , False )

W , H = 720 , 480 
RUN = True

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Kavosh Maze')

main_page = pygame.image.load("Pages/main.png")
maze_page = pygame.image.load("Pages/maze4.png")

maze_config = {"Position" : [5 , 5] , "Block Size" : 50 , "Color" : (0 , 0 , 0)}
maze_file = "maze.png"
maze_write = "maze2.png"

vitcims = { 'H' : pygame.image.load("Pages/H.png") ,
            'S' : pygame.image.load("Pages/S.png") ,
            'U' : pygame.image.load("Pages/U.png") ,
            'Red' : pygame.image.load("Pages/Red.png") ,
            'Green' : pygame.image.load("Pages/Green.png") ,
            'Yellow' : pygame.image.load("Pages/Yellow.png") ,
}

# [ X , Y ] : {visited : true/false , past_block : (X , Y) ,  walls = [ ]}
blocks = {}

past_block = [0 , 0 ]
current_block = [0 , 0]

count = 0
complete = False


pages = [main_page , maze_page ]
page = 0

start_button = [(290 , 390) , (430 , 430)]
finish_button = [(300 , 20) , (400 , 50)]
restart_buttton = [(600 , 20) , (700 , 50)]

start_time = 0

if __name__ == "__main__" :  

    cv.imwrite("maze2.png",cv.imread("maze base.png"))
    cv.imwrite("maze.png",cv.imread("maze base.png"))

    Maze = threading.Thread(target=maze)
    Maze.start()

    while RUN :
        update_screen(pages[page] , start_time)
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                RUN = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q :
                    RUN = False

            if event.type == pygame.MOUSEBUTTONUP:
                clicked(pygame.mouse.get_pos())

    pygame.quit()


