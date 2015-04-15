import itertools
import time
import serial
import pypot.vrep
from pypot.vrep import from_vrep
from poppy.creatures import PoppyHumanoid




pypot.vrep.close_all_connections()

poppy = PoppyHumanoid(simulator='vrep') #connection à simulateur
print ('Connection reussi avec POPPY HUMANOID') 

poppy.compliant = False
poppy.power_up()

        # Change PID of Dynamixel MX motors
for m in filter(lambda m: hasattr(m, 'pid'), poppy.motors):
    m.pid = (1, 8, 0)  #4,2,0

for m in poppy.torso:
    m.pid = (6, 2, 0)

        # Reduce max torque to keep motor temperature low
for m in poppy.motors:
    m.torque_limit = 70

time.sleep(0.5)


ser = serial.Serial(
	port='COM5',
	baudrate=115200,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_TWO
)


x = ser.write("hola mundo PYSERIAL")
i=1
while i==1 :
    lectura = ser.readline()

    ser.flushInput()
    if (len(lectura)==20):
        dato1=float(lectura[0]+lectura[1]+lectura[2]+lectura[3])  # " , " 
        dato2=float(lectura[5]+lectura[6]+lectura[7]+lectura[8])  # " , " 
        dato3=float(lectura[10]+lectura[11]+lectura[12]+lectura[13])  # " , " 
        dato4=float(lectura[15]+lectura[16]+lectura[17]+lectura[18])  # " , " 
        poppy.l_shoulder_y.goal_position = dato1
        poppy.l_shoulder_x.goal_position =dato2
        poppy.l_arm_z.goal_position = dato3
        poppy.l_elbow_y.goal_position =dato4
        print (dato1)
        print (dato2)
        print (dato3)
        print (dato4)


 
    
print ('Fin')




ser.close # fermé la connection serial
poppy.close()  # fermé la connection avec poppy