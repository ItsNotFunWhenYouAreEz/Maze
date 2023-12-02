import serial
from CalcLidarData import CalcLidarData
import time


ser = serial.Serial(port='COM9',
                    baudrate=230400,
                    bytesize=8,
                    parity='N',
                    stopbits=1)



def get_walls(angle) :
    tmpString = ""
    lines = list()
    angles = list()
    distances = list()

    cnt = 0
    i = 0

    walls = {"UP" : 0 , "DOWN" : 0 , "RIGHT" : 0 , "LEFT" : 0 }

    while True:
        loopFlag = True
        flag2c = False

        if(i  % 40 == 39):
            i = 0


            angles =  [round(elem) for elem in angles ]



            for i in range( , 272) :

                try :
                    L = 1 if distances[angles.index(i)] < 20 else 0 
                    break
                except :
                    pass

            for i in range(88 , 92) :

                try :
                    R = 1 if distances[angles.index(i)]  < 20 else 0 
                    break
                except :
                    pass

            for i in range(angle , angle + 5) :

                try :
                    U = 1 if distances[angles.index(i)] < 20 else 0
                    break
                except :
                    pass

            for i in range(178 , 182) :

                try :
                    D = 1 if distances[angles.index(i)]  < 20 else 0
                    break
                except :
                    pass
            
            walls = {"UP" : U , "DOWN" : D , "RIGHT" : R , "LEFT" : L }

            return walls



        while loopFlag:
            b = ser.read()
            tmpInt = int.from_bytes(b, 'big')
            if (tmpInt == 0x54):
                tmpString +=  b.hex()+" "
                flag2c = True
                continue

            elif(tmpInt == 0x2c and flag2c):
                tmpString += b.hex()

                if(not len(tmpString[0:-5].replace(' ','')) == 90 ):
                    tmpString = "" 
                    loopFlag = False
                    flag2c = False
                    continue

                lidarData = CalcLidarData(tmpString[0:-5])
                angles.extend(lidarData.Angle_i)
                distances.extend(lidarData.Distance_i)

                tmpString = ""
                loopFlag = False
                cnt += len(lidarData.Distance_i)

            else:
                tmpString += b.hex()+" "
            
            flag2c = False
        i += 1
