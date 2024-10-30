

import rospy

if __name__ == '__main__':

    rospy.init_node('param_del')
    
    try:
        rospy.delete_param('type')
        rospy.delete_param('radius')
        rospy.loginfo('param deleted')
    except Exception as e:
        rospy.loginfo('param does not exist')

    
    
