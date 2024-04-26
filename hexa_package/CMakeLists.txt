cmake_minimum_required(VERSION 3.5)
project(hexa_package)

# Find packages
find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Generate ROS 2 services
# set(srv_files srv/MyService.srv)
# rosidl_generate_interfaces(${PROJECT_NAME} ${srv_files} )

# Install targets
# install( DIRECTORY srv DESTINATION share/${PROJECT_NAME} )

ament_package()

# rosparam set robot_description -t /path/to/your/urdf/file.urdf
# rosrun robot_state_publisher robot_state_publisher
# chmod +x custom_robot_state_publisher.py

#

#chmod +x src/your_script.py
#cd ~/catkin_ws  # Your catkin workspace
#catkin_make
#source devel/setup.bash
#roslaunch my_package my_launch_file.launch
