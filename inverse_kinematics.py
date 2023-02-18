import ikpy.chain
import numpy as np
import math
import serial


my_chain = ikpy.chain.Chain.from_urdf_file("arm_urdf.urdf",active_links_mask=[False, True, True, True, True, True, True]) # base +6 segments


target_position = [ 0, 0,0.58]# x,y,z poistion of the end effector
target_orientation = [-1, 0, 0] # x,y,z orientation of the end effector


ik = my_chain.inverse_kinematics(target_position, target_orientation, orientation_mode="Y")
print("The angles of each joints are : ", list(map(lambda r:math.degrees(r),ik.tolist())))


# computed_position = my_chain.forward_kinematics(ik)
# print("Computed position: %s, original position : %s" % (computed_position[:3, 3], target_position))
# print("Computed position (readable) : %s" % [ '%.2f' % elem for elem in computed_position[:3, 3] ])


#ser = serial.Serial('COM3',9600, timeout=1)

def sendCommand(a,b,c,d,e,f,move_time):
    command = '0{:.2f} 1{:.2f} 2{:.2f} 3{:.2f} 4{:.2f} 5{:.2f} t{:.2f}\n'.format(math.degrees(a),math.degrees(b),math.degrees(c),math.degrees(d),math.degrees(e),math.degrees(f),move_time)
    #ser.write(command.encode('ASCII'))
    print(command)

def doIK():
    global ik
    old_position= ik.copy()
    ik = my_chain.inverse_kinematics(target_position, target_orientation, orientation_mode="Z", initial_position=old_position)

   
def move(x,y,z):
    global target_position
    target_position = [x,y,z]
    doIK()
    sendCommand(ik[1].item(),ik[2].item(),ik[3].item(),ik[4].item(),ik[5].item(),ik[6].item(),1)

def move(x,y,z,a,b,c):
    global target_position
    target_position = [x,y,z]
    target_orientation = [a,b,c]
    doIK()
    sendCommand(ik[1].item(),ik[2].item(),ik[3].item(),ik[4].item(),ik[5].item(),ik[6].item(),1)

def rotate(x,y,z):
    global target_orientation
    target_orientation = [x,y,z]
    doIK()
    sendCommand(ik[1].item(),ik[2].item(),ik[3].item(),ik[4].item(),ik[5].item(),ik[6].item(),1)



