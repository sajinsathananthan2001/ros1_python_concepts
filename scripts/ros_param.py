#!/usr/bin/env python

import rospy

# Initialize the ROS node
rospy.init_node('parameter_example', anonymous=True)

# Set a parameter
rospy.set_param('/example_param', 'Hello, ROS!')

# Get the parameter value
param_value = rospy.get_param('/example_param', default="Parameter not set")
rospy.loginfo("Value of '/example_param': %s", param_value)

# Shutdown the node
rospy.signal_shutdown("Example complete")
