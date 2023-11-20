import serial
import binascii
from CalcLidarData import CalcLidarData
import matplotlib.pyplot as plt
import math

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='polar')
ax.set_title('lidar (exit: Key E)',fontsize=18)


plt.connect('key_press_event', lambda event: exit(1) if event.key == 'e' else None)

ser = serial.Serial(port='COM9',
                    baudrate=230400,
                    bytesize=8,
                    parity='N',
                    stopbits=1)

tmpString = ""
lines = list()
angles = list()
distances = list()

cnt = 0
i = 0


while True:
    loopFlag = True
    flag2c = False

    if(i  % 40 == 39):
        i = 0

        plt.pause(0.01)
        angles =  [round(elem) for elem in angles ]
        try :
            print(distances[angles.index(1)])
            file = open("data.txt" , "a")
            file.write(distances)
            file.write("\n")
            file.write(angles)
            file.close()
        except :
            pass
        angles.clear()
        distances.clear()
        

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


ser.close()