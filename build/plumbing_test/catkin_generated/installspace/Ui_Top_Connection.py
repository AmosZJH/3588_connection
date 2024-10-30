import sys


sys.path.append("./src/plumbing_test/src")
sys.path.append("./src/plumbing_test/scripts")

print(sys.path) #帮助查看导包是否正常,很重要，rosrun和vscode运行的路径是不一样的

import rospy
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog,QMainWindow
import serial


from Ui_test import Ui_MainWindow
from uservo import UartServoManager
from plumbing_test.msg import Servo

# SERVO_PORT_NAME = "/dev/ttyUSB0"
# SERVO_BAUDRATE = 115200

# uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
#                      parity=serial.PARITY_NONE, stopbits=1,\
#                      bytesize=8,timeout=0)#初始化串口

# uservo = UartServoManager(uart)

rospy.init_node('servo_control')

pub = rospy.Publisher('servo',Servo,queue_size=10)

p1 = Servo() #初始化消息，后续是否有可能写到class里面
p2 = Servo()
p3 = Servo()
p4 = Servo()



p1.servo_id = 1
p1.angle = -66      #默认角度
p1.speed = 100.0    #默认速度

p2.servo_id = 2
p2.angle = -81
p2.speed = 100.0    

p3.servo_id = 3
p3.angle = 16
p3.speed = 100.0


p4.servo_id = 4
p4.angle = -10
p4.speed = 100.0






class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

        self.pushButton.clicked.connect(self.setangle_1)   #写入1号舵机角度
        self.pushButton_2.clicked.connect(self.setangle_2) #写入2号舵机角度
        self.pushButton_3.clicked.connect(self.setangle_3) #写入3号舵机角度
        self.pushButton_4.clicked.connect(self.setangle_4) #写入4号舵机角度

        self.pushButton_6.clicked.connect(self.resetangle) #重置舵机角度


        self.pushButton_5.clicked.connect(self.qureyangle) #查询舵机角度

        
    def setangle_1(self):
        angle_1 = self.textEdit.toPlainText()
        p1.angle = int(angle_1)
        pub.publish(p1)
        rospy.loginfo("angle_1: %s",angle_1)

        # if self.textEdit_5.toPlainText() == "":
        #     uservo.set_servo_angle(1, int(angle_1), False, None, None, 20, 20, 0, 100.0)
            
        # else:
        #     speed = self.textEdit_5.toPlainText()
        #     uservo.set_servo_angle(1, int(angle_1), False, None, None, 20, 20, 0, float(speed))
    
    def setangle_2(self):
        angle_2 = self.textEdit_2.toPlainText()
        p2.angle = int(angle_2)
        pub.publish(p2)
        rospy.loginfo("angle_2: %s",angle_2)
        # if self.textEdit_6.toPlainText() == "":
        #     uservo.set_servo_angle(2, int(angle_2), False, None, None, 20, 20, 0, 100.0)
        # else:
        #     speed = self.textEdit_6.toPlainText()
        #     uservo.set_servo_angle(2, int(angle_2), False, None, None, 20, 20, 0, float(speed))



    def setangle_3(self):
        angle_3 = self.textEdit_3.toPlainText()
        p3.angle = int(angle_3)
        pub.publish(p3)
        rospy.loginfo("angle_3: %s",angle_3)
        # if self.textEdit_7.toPlainText() == "":
        #     uservo.set_servo_angle(3, int(angle_3), False, None, None, 20, 20, 0, 100.0)
        # else:
        #     speed = self.textEdit_7.toPlainText()
        #     uservo.set_servo_angle(3, int(angle_3), False, None, None, 20, 20, 0, float(speed))

    def setangle_4(self):
        angle_4 = self.textEdit_4.toPlainText()
        p4.angle = int(angle_4)
        pub.publish(p4)
        rospy.loginfo("angle_4: %s",angle_4)
        # if self.textEdit_8.toPlainText() == "":
        #     uservo.set_servo_angle(4, int(angle_4), False, None, None, 20, 20, 0, 100.0)
        # else:
        #     speed = self.textEdit_8.toPlainText()
        #     uservo.set_servo_angle(4, int(angle_4), False, None, None, 20, 20, 0, float(speed))
    
    def resetangle(self):
        #uservo.set_servo_angle(1, -66, False, None, None, 20, 20, 0, 100.0)
        p1.angle = -66
        
        #uservo.set_servo_angle(2, -81, False, None, None, 20, 20, 0, 100.0)
        p2.angle = -81
        
        #uservo.set_servo_angle(3, 16, False, None, None, 20, 20, 0, 100.0)
        p3.angle = 16
        
        #uservo.set_servo_angle(4, -10, False, None, None, 20, 20, 0, 100.0)
        p4.angle = -10


    def qureyangle(self):
        pass
        # servo_angle=[0,0,0,0]
        # i=0
        # while i <4:
        #     servo_angle[i] = uservo.query_servo_angle(i+1)
        #     i+=1
        
        # self.display(servo_angle)         #显示舵机角度

    def display(self,result):             #关联函数
         
        self.textBrowser_2.setText(str(result[0]))
        self.textBrowser_3.setText(str(result[1]))
        self.textBrowser_4.setText(str(result[2]))
        self.textBrowser_5.setText(str(result[3]))
    
    




        



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    
    
    
    
    
   
   #循环等待
    sys.exit(app.exec_()) 