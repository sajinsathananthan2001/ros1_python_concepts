#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty,EmptyResponse
from geometry_msgs.msg import Twist


def empty_response_cb(req):
    print("Executed the service!")

    rate = rospy.Rate(2)
    obj = Twist()

    for i in range(10):

        
        obj.angular.z = 0.5
        obj.linear.x = 1

        pub.publish(obj)

        rate.sleep()

    return EmptyResponse


def service_node():
    rospy.init_node("turtle_run_service")
    rospy.logwarn("Starting server!")

    global pub
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    server = rospy.Service('run_the_turtle',Empty,empty_response_cb)
    

    rospy.spin()

if __name__ == '__main__':
    try:
        
        service_node()
    except rospy.ROSInterruptException:
        pass