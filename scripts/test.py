import socket
import time
from ctypes import *

'''
A simple example for controlling a single joint move once by python

Ref: https://github.com/MrAsana/AMBER_B1_ROS2/wiki/SDK-&-API---UDP-Ethernet-Protocol--for-controlling-&-programing#2-single-joint-move-once
C++ version:  https://github.com/MrAsana/C_Plus_API/tree/master/amber_gui_4_node
     
'''
#IP_ADDR = "192.168.50.235"
# ROS master's IP address
IP_ADDR = "127.0.0.1"


#IP_ADDR = "127.0.0.1"  # ROS master's IP address

class robot_joint_position(Structure):  # ctypes struct for send
    _pack_ = 1  # Override Structure align
    _fields_ = [("cmd_no", c_uint16),  # Ref:https://docs.python.org/3/library/ctypes.html
                ("length", c_uint16),
                ("counter", c_uint32),
                ("pos0", c_float),
                ("pos1", c_float),
                ("pos2", c_float),
                ("pos3", c_float),
                ("pos4", c_float),
                ("pos5", c_float),
                ("pos6", c_float),
                ("pos7", c_float),
                ("time", c_float),
                ]


class robot_mode_data(Structure):  # ctypes struct for receive
    _pack_ = 1
    _fields_ = [("cmd_no", c_uint16),
                ("length", c_uint16),
                ("counter", c_uint32),
                ("respond", c_uint8),
                ]


class gripper_ctrl(Structure):  # ctypes struct for send
    _pack_ = 1  # Override Structure align
    _fields_ = [("cmd_no", c_uint16),  # Ref:https://docs.python.org/3/library/ctypes.html
                ("length", c_uint16),
                ("counter", c_uint32),
                ("action", c_uint16),  # Ref:https://docs.python.org/3/library/ctypes.html
                ("intensity", c_uint16),
                ("version", c_bool)
                ]




def moveJ(j1, j2, j3, j4, j5, j6, j7, j8, t):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Standard socket processes
    s.bind(("0.0.0.0", 12322))

    payloadS = robot_joint_position(4, 44, 114514, j1, j2, j3, j4, j5, j6, j7, j8, t)
    s.sendto(payloadS, (IP_ADDR, 26001))  # Default port is 25001
    print("Sending: cmd_no={:d}, "
          "length={:d}, counter={:d},".format(payloadS.cmd_no,
                                              payloadS.length,
                                              payloadS.counter, ))

    print("pos0={:f},pos1={:f},pos2={:f},"
          "pos3={:f},pos4={:f},"
          "pos5={:f},pos6={:f},"
          "pos7={:f},time={:f}".format(payloadS.pos0, payloadS.pos1,
                                       payloadS.pos2, payloadS.pos3,
                                       payloadS.pos4, payloadS.pos5,
                                       payloadS.pos6, payloadS.pos7,
                                       payloadS.time))

    s.settimeout(0.5)
    try:

        data, addr = s.recvfrom(1024)  # Need receive return
        print("Receiving: ", data.hex())
        payloadR = robot_mode_data.from_buffer_copy(data)  # Convert raw data into ctypes struct to print
        print("Received: cmd_no={:d}, length={:d}, "
              "counter={:d}, respond={:d}".format(payloadR.cmd_no,
                                                  payloadR.length,
                                                  payloadR.counter,
                                                  payloadR.respond, ))
    except socket.timeout:
        print("timeout!")
    s.close()
def gripper(isClose):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Standard socket processes
    s.bind(("0.0.0.0", 12322))

    payloadS = gripper_ctrl(9, 13, 114514, isClose, 10, 0)  # 0 : open, 1 : close
    s.sendto(payloadS, (IP_ADDR, 26001))  # Default port is 25001
    print("Sending: cmd_no={:d}, "
          "length={:d}, counter={:d},".format(payloadS.cmd_no,
                                              payloadS.length,
                                              payloadS.counter, ))

    print("Action={:d},Intensity={:d},Version={:d}".format(payloadS.action, payloadS.intensity, payloadS.intensity))

    s.settimeout(0.5)
    try:

        data, addr = s.recvfrom(1024)  # Need receive return
        print("Receiving: ", data.hex())
        payloadR = robot_mode_data.from_buffer_copy(data)  # Convert raw data into ctypes struct to print
        print("Received: cmd_no={:d}, length={:d}, "
              "counter={:d}, respond={:d}".format(payloadR.cmd_no,
                                                  payloadR.length,
                                                  payloadR.counter,
                                                  payloadR.respond, ))
    except socket.timeout:
        print("timeout!")
    s.close()
    time.sleep(3)

moveJ(0,0,0,0,0,0,0,0,4)
while True:
    moveJ(1, 1, 1, 1, 1, 1, 0, 0, 3)
    time.sleep(4)
    moveJ(-1,-1,-1,-1,-1,-1,-1,0, 3)
    time.sleep(4)
    #moveJ(-1.076839, 0.090266, 0.475466, -1.142918, -1.380309, 0.94378, -0.548279, 0, 1)
    #time.sleep(2)
    #gripper(0)
    #time.sleep(2)
    #moveJ(-1.076839, 0.090266, 1, -1.142918, -1.380309, 1.5 , -0.548279, 0, 1)
    #time.sleep(1)
    #moveJ(0, 0, 0, 0, 0, 0,0, 0, 1)
    #time.sleep(2)
    #moveJ(-1.076839, 0.090266, 1, -1.142918, -1.380309, 1.5 , -0.1548279, 0, 1)
    #time.sleep(1)
    #moveJ(-1.076839, 0.090266, 0.475466, -1.142918, -1.380309, 0.94378, -0.548279, 0, 1)
    #time.sleep(2)
    #gripper(1)
    #time.sleep(2)
    #moveJ(-0.608243, -0.453104, 0.701268, 0.807896, -1.902272, 1.6, -0.548279, 0, 1)
    #gripper(0)
    #time.sleep(2)
    #gripper(1)
    #time.sleep(2)


