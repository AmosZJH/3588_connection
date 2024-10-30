 

import rospy

if __name__ == '__main__':
    rospy.init_node('param_get')

    #1.get_param
    radius = rospy.get_param('radius',0.5)
    radius2 = rospy.get_param('radius_p_xx',0.5)
    rospy.loginfo('radius:%.2f', radius)
    rospy.loginfo('radius2:%.2f', radius2)


    #2.get_param_cached
    radius3 = rospy.get_param_cached('radius',0.2)
    radius4 = rospy.get_param_cached('radius_p_xx',0.5)
    rospy.loginfo('radius:%.2f', radius3)
    rospy.loginfo('radius2:%.2f', radius4)

    #3.get_param_names
    names = rospy.get_param_names()

    for name in names:
        rospy.loginfo('name:%s', name)

    #4 has_param
    flag1 = rospy.has_param('radius')
    if flag1:
        rospy.loginfo('has param radius')