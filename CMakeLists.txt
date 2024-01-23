cmake_minimum_required(VERSION 3.0.2)
project(ros1_python_concepts)


find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs  
  message_generation      

)



## Generate services in the 'srv' folder
add_service_files(

  FILES
  addition.srv
  
)


generate message(
  DEPENDENCIES
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES ros1_python_concepts
#  CATKIN_DEPENDS rospy
#  DEPENDS system_lib
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

