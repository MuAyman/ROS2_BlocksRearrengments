cmake_minimum_required(VERSION 3.5)
project(CPPsub_BlocksRearrange)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# Include directories
include_directories(include)

# Add executable
add_executable(lis src/CPPsub_BlocksRearrange.cpp src/BFSAlgorithm.cpp src/StateSpace.cpp)

# Link libraries
ament_target_dependencies(lis rclcpp std_msgs)

# Install
install(TARGETS
  lis
  DESTINATION lib/${PROJECT_NAME})


ament_package()
