cmake_minimum_required(VERSION 3.0.2)
project(ros1_python_concepts)


find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs  
  message_generation      

)

find_package(Boost REQUIRED COMPONENTS system)



## Generate services in the 'srv' folder
add_service_files(

  FILES
  addition.srv
  velocity.srv
  practice.srv
  
  
)


generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package()


include_directories(

  ${catkin_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIRS}
)


