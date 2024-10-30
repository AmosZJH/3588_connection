#!/usr/bin/env python3

import rospy

from connection.msg import Person


def doPerson(msg):
    rospy.loginfo("receive message: %s, %d, %.2f", msg.name, msg.age, msg.height)
    pass


if __name__ == "__main__":

    rospy.init_node("subscriber_node_3")

    sub = rospy.Subscriber("person", Person, doPerson, queue_size=10)

    rospy.spin()


    pass