#!/usr/bin/env python3

import rospy   

from connection.msg import Person



if __name__ == '__main__':
    
    rospy.init_node("publisher_node_3")

    pub = rospy.Publisher("person", Person, queue_size=10)  #发布的消息类型为Person

    p = Person()
    p.name = "Tom"
    p.age = 18
    p.height = 1.75

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        pub.publish(p)
        
        rospy.loginfo("send message: %s, %d, %.2f", p.name, p.age, p.height)
        rate.sleep()



    pass
