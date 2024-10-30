#!/usr/bin/env python3

import rospy
from std_msgs.msg import String 


def doMsg(msg):
    rospy.loginfo("receive message: %s", msg.data)
    pass

if __name__ == '__main__':

    rospy.init_node("connection_node_2")

    sub = rospy.Subscriber("ceshi", String, doMsg, queue_size=10)

    rospy.spin()

    
    pass