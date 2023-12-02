#from lidar import get_walls

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
        walls = blocks[tuple(current_block)]["walls"]
        print(walls)
        print(current_block , past_block)
        print("----------")
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

# [ X , Y ] : {visited : true/false , past_block : (X , Y) ,  walls = [ ]}
blocks = {}

past_block = [0 , 0 ]
current_block = [0 , 0]

count = 0
complete = False

angel = 0

if __name__ == "__main__" : 
    while True :
        print(angel)
        print(current_block)    
        
        walls = list(map(int , input("UP DOWN RIGHT LEFT \n").split()))
        walls = {"UP" : walls[0] , "DOWN" : walls[1] , "RIGHT" : walls[2] , "LEFT" : walls[3]}
        next_block(walls)
        print(blocks)

        if complete :
            print("Finish")
            break

    print(count)
