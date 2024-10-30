import sys


sys.path.append("./src/plumbing_test/src")
sys.path.append("./src/plumbing_test/scripts")

print(sys.path) #帮助查看导包是否正常,很重要，rosrun和vscode运行的路径是不一样的

import rospy
import serial



from uservo import UartServoManager
from plumbing_test.msg import Servo

SERVO_PORT_NAME = "/dev/ttyUSB0"
SERVO_BAUDRATE = 115200

uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
                     parity=serial.PARITY_NONE, stopbits=1,\
                     bytesize=8,timeout=0)#初始化串口

uservo = UartServoManager(uart)




def control_servo(msg):

    uservo.set_servo_angle(servo_id=msg.servo_id, angle=msg.angle, mean_dps=msg.speed)
    print(msg.servo_id)
    print(msg.angle)
    print(msg.speed)


if __name__ == '__main__':

    rospy.init_node('sub_3588')

    sub = rospy.Subscriber('servo', Servo, control_servo)

    rospy.spin()