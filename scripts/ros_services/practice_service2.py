#!/usr/bin/env python3

import rospy

from ros1_python_concepts.srv import practice


def empty_cb(empty):
    rospy.loginfo("EmpyResponse!")
    return "None"
    


def perform():

    service = rospy.Service('empty_req_respond', practice, empty_cb)



if __name__=="__main__":

    rospy.init_node('practice_service2')

    perform()

    rospy.spin()