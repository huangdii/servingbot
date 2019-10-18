cmake_minimum_required(VERSION 2.8.3)
project(servebot)

#켓킨을 찾고 켓킨 패키지를 찾음
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs genmsg sensor_msgs)

## Declare catkin package
catkin_package()

include_directories(include ${catkin_INCLUDE_DIRS})

#빌드
add_executable(zed_depth_pos_sub src/depth_subscribe.cpp)

# 라이브라리에 올리기 
target_link_libraries(zed_depth_pos_sub ${catkin_LIBRARIES})















