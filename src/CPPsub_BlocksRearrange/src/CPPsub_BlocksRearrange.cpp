#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

// #include "BlockArrangmentAlgorithm.hpp"
#include "../include/CPPsub_BlocksRearrange/BlockArrangmentAlgorithm.hpp"


using std::placeholders::_1;

class blockArrangementSub : public rclcpp::Node
{
  public:
    blockArrangementSub()
    : Node("BlockArrange_subscriber")
    {
      subscription_ = this->create_subscription<std_msgs::msg::String>(
      "initGoalTopic", 13, std::bind(&blockArrangementSub::topic_callback, this, _1));
    }

  private:
    void topic_callback(const std_msgs::msg::String::SharedPtr msg) const
    {
      RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
      // BFSAlgorithm solve(msg->data.c_str())

    }
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<blockArrangementSub>());
  rclcpp::shutdown();
  return 0;
}