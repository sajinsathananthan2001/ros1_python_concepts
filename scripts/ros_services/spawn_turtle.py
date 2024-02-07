#!/usr/bin/env python3 
 
import rospy
from turtlesim.srv import Spawn, SpawnRequest
 
def spawn_turtle_client(x, y, theta, name):
    rospy.wait_for_service('/spawn')
    try:
        spawn_turtle = rospy.ServiceProxy('/spawn', Spawn)
        server_response = spawn_turtle(x, y, theta, name)
        return server_response.name
    except rospy.ServiceException as e:
        print("Service call failes: %s"%e)
 
     
if __name__=="__main__":
    rospy.init_node("my_client_node")
    rate = rospy.Rate(10)
 
    print("Calling Spawn Service!")
    service_response = spawn_turtle_client(2.0, 1.0, 0.0, "Lentin")
    print("Turtle %s has spawned!"%service_response)
 
    while not rospy.is_shutdown():
        rate.sleep()
