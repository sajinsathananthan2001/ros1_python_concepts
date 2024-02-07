#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

if __name__ == __main__:

    rospy.init_node("turtle_controller")
    rospy.loginfo("Controller Started")

