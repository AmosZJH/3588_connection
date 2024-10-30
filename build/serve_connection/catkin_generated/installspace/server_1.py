
import rospy

from serve_connection.srv import Addints, AddintsRequest, AddintsResponse  


def handle_addints(req):


    num1 = req.num1
    num2 = req.num2

    sum = num1 + num2

    response = AddintsResponse()
    response.sum = sum

    rospy.loginfo("服务器正在解析请求，返回结果为：%s" % sum)
    return response

if __name__ == '__main__':
    
    rospy.init_node('server_1')

    server = rospy.Service('addints', Addints, handle_addints)
    rospy.loginfo("Server is ready to add two ints.")

    rospy.spin()