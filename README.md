# ROS2 Blocks Rearrangement

## About
ROS2 Blocks Rearrangement is a project aimed at demonstrating block rearrangement using ROS2. It consists of two main components: a Python publisher node (`initialGoalpub_py`) and a C++ subscriber node (`CPPsub_BlocksRearrange`).

## InitialGoalpub_py
The `initialGoalpub_py` node publishes initial goal configurations and optimal movements to the `initGoalTopic`.

## CPPsub_BlocksRearrange
The `CPPsub_BlocksRearrange` node subscribes to the `initGoalTopic`, receives the data, and processes it using the BFS algorithm to rearrange the blocks accordingly.

## Installation
To install the required dependencies, run the following commands:

```bash
# Install ROS2
sudo apt update
sudo apt install ros-foxy-desktop

# Build the workspace
cd <your_workspace>
colcon build
source install/setup.bash
```

## Usage
To run the nodes, use the following commands:

```bash
# Run the publisher node
ros2 run initialGoalpub_py initialGoalpub_py

# Run the subscriber node
ros2 run CPPsub_BlocksRearrange CPPsub_BlocksRearrange
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.
