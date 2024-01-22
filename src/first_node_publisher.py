#!/usr/bin/env python3


import rospy
from std_msgs.msg import String


def publisher():
    
    rospy.init_node('first_node',anonymous=True)
    
    pub = rospy.Publisher('fake_data_string',String,queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        fake_data = "Hello world!"

        #rospy.loginfo(fake_data)

        pub.publish(fake_data)

        rate.sleep()




if __name__ == '__main__':

    try:
        publisher()

    except rospy.ROSInterruptException:
        pass