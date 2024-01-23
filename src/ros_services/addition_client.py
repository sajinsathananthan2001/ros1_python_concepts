#!/usr/bin/env python3

import sys 
import rospy
from ros1_python_concepts.srv import addition


def add__two_ints_client(x,y):
    rospy.wait_for_service('add_two_ints')
    add_two_ints = rospy.ServiceProxy('add_two_ints',addition)
    resp1 = add_two_ints(x,y)
    print(resp1.result)
    return resp1.result


if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    add__two_ints_client(x,y)