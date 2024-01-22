#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty,EmptyResponse

def empty_response_cb(req):
    print("Just a service!")
    return EmptyResponse

def service_node():
    rospy.init_node("empty_server_service")
    rospy.logwarn("Starting empty server!")
    server = rospy.Service('print_service',Empty,empty_response_cb)

    rospy.spin()

if __name__ == '__main__':
    try:
        service_node()
    except rospy.ROSInterruptException:
        pass