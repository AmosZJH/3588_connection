
import sys
import rospy


from serve_connection.srv import Addints, AddintsRequest, AddintsResponse

if __name__ == '__main__':

    if len(sys.argv) != 3:
        rospy.loginfo("请输入两个整数")
        sys.exit(1)
        

    rospy.init_node('client_1')

    client = rospy.ServiceProxy('addints', Addints)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    #client.wait_for_service()
    rospy.wait_for_service('addints')


    reponse = client.call(num1,num2)



    rospy.loginfo("服务器返回的结果为：%s" % reponse.sum)

    pass