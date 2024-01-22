#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def data_callback(data):
    rospy.loginfo(data)

def subscriber():
    rospy.init_node('subscriber')

    rospy.Subscriber('fake_data_string',String,data_callback,queue_size=10)

    rospy.spin()


if __name__ == '__main__':

    try:
        subscriber()

    except rospy.ROSInterruptException:
        pass