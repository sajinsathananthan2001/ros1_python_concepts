#!/usr/bin/env python3

import sys 
import rospy
from ros1_python_concepts.srv import addition


def add__two_ints_client(x,y):
    rospy.wait_for_service('add_two_ints')
    data = rospy.ServiceProxy('add_two_ints',addition)
    resp1 = data(x,y)
    print(resp1.result)
    return resp1.result


if __name__ == "__main__":
    x = 474
    y = 34

    add__two_ints_client(x,y)