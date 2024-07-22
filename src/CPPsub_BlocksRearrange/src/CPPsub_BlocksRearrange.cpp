#include <memory>
#include <iostream>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

#include "../include/CPPsub_BlocksRearrange/BFSAlgorithm.h"
#include "../include/CPPsub_BlocksRearrange/StateSpace.h"


using std::placeholders::_1;

class blockArrangementSub : public rclcpp::Node
{
public:
  blockArrangementSub() : Node("BlockArrange_subscriber")
  {
    subscription_ = this->create_subscription<std_msgs::msg::String>(
        "initGoalTopic", 13, std::bind(&blockArrangementSub::topic_callback, this, _1));
  };

private:
  void topic_callback(const std_msgs::msg::String::SharedPtr msg) const
  {
    std::string message = msg->data.c_str();

    // Initialize BFSAlgorithm with the received message
    BFSAlgorithm sol(message); // Assuming the constructor accepts std::string

    // Run BFS Algorithm
    Moves path = sol.BFS_Algorithm();

    // Compare results
    sol.compare();
  }

  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

int main(int argc, char *argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<blockArrangementSub>());
  rclcpp::shutdown();
  return 0;
}
