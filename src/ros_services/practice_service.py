#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

from ros1_python_concepts.srv import velocity , velocityResponse

data_obj = Twist()

def velocity_change_cb(req):
    #publish the req vel and angle 
    data_obj.linear.x = req.vel
    data_obj.angular.z = req.angle

    pub.publish(data_obj)


def perform():

    service = rospy.Service('velocity_change_service', velocity, velocity_change_cb)

    global pub
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)


if __name__=="__main__":

    rospy.init_node('practice_service')

    perform()

    rospy.spin()