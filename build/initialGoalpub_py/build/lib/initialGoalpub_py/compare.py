import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class InitialGoalPub(Node):
    def __init__(self):
        super().__init__('initial_goal_pub')
        self.publisher_ = self.create_publisher(String, 'initial_goal_topic', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        msg = String()
        data = self.get_dataaa()
        if data is not None:
            initial, goal, optimal = data
            msg.data = self.lists_to_string(initial, goal, optimal)
            self.publisher_.publish(msg)
            self.get_logger().info(f'Publishing: {msg.data}')
            self.counter += 1
        else:
            self.get_logger().info('All test cases published, shutting down.')
            self.destroy_node()

    def lists_to_string(self, initial, goal, optimal):
        initial_str = 'Initial: ' + str(initial)
        goal_str = 'Goal: ' + str(goal)
        optimal_str = 'Optimal: ' + str(optimal)
        return initial_str + ' | ' + goal_str + ' | ' + optimal_str

    def get_dataaa(self):
        counter = self.counter
        if counter == 0:
            initial_arrangement_0 = [['B', 'D', 'F'], ['C', 'E'], ['A']]
            goal_arrangement_0 = [['A', 'C', 'D'], ['B', 'E'], ['F']]
            optimal_movements_0 = [('C', 'Table'), ('B', 'Table'), ('D', 'C'), ('E', 'B'), ('A', 'Table'), ('C', 'A'), ('B', 'Table'), ('E', 'B'), ('D', 'Table'), ('C', 'D'), ('B', 'Table'), ('F', 'B')]
            return [initial_arrangement_0, goal_arrangement_0, optimal_movements_0]
        elif counter == 1:
            initial_arrangement_1 = [['C', 'A', 'F'], ['B', 'E'], ['D']]
            goal_arrangement_1 = [['A', 'B', 'C'], ['D', 'E'], ['F']]
            optimal_movements_1 = [('D', 'Table'), ('C', 'Table'), ('E', 'Table'), ('B', 'E'), ('A', 'Table'), ('B', 'A'), ('C', 'Table'), ('A', 'C'), ('B', 'Table'), ('E', 'B'), ('F', 'Table'), ('B', 'F')]
            return [initial_arrangement_1, goal_arrangement_1, optimal_movements_1]
        elif counter == 2:
            initial_arrangement_2 = [['E', 'C', 'A'], ['B', 'D', 'F']]
            goal_arrangement_2 = [['A', 'B', 'C'], ['D', 'E'], ['F']]
            optimal_movements_2 = [('D', 'Table'), ('E', 'Table'), ('F', 'Table'), ('D', 'F'), ('C', 'Table'), ('B', 'C'), ('A', 'Table'), ('B', 'A'), ('C', 'Table'), ('A', 'C'), ('B', 'Table'), ('E', 'B')]
            return [initial_arrangement_2, goal_arrangement_2, optimal_movements_2]
        elif counter == 3:
            initial_arrangement_3 = [['G', 'D', 'A'], ['C', 'B', 'F'], ['E']]
            goal_arrangement_3 = [['A', 'B', 'C'], ['D', 'E'], ['F'], ['G']]
            optimal_movements_3 = [('E', 'Table'), ('F', 'Table'), ('B', 'Table'), ('C', 'Table'), ('D', 'Table'), ('G', 'Table'), ('A', 'Table'), ('B', 'A'), ('C', 'B'), ('A', 'C'), ('D', 'Table'), ('E', 'D'), ('F', 'Table'), ('E', 'F'), ('G', 'Table')]
            return [initial_arrangement_3, goal_arrangement_3, optimal_movements_3]
        elif counter == 4:
            initial_arrangement_4 = [['F', 'A'], ['B', 'E', 'D'], ['C']]
            goal_arrangement_4 = [['A', 'B', 'C'], ['D', 'E'], ['F']]
            optimal_movements_4 = [('D', 'Table'), ('C', 'Table'), ('E', 'Table'), ('D', 'E'), ('A', 'Table'), ('B', 'A'), ('F', 'Table'), ('B', 'F'), ('C', 'Table'), ('B', 'C'), ('A', 'Table'), ('E', 'A')]
            return [initial_arrangement_4, goal_arrangement_4, optimal_movements_4]
        elif counter == 5:
            initial_arrangement_5 = [['A', 'C'], ['D', 'E'], ['B', 'F']]
            goal_arrangement_5 = [['A', 'B', 'C'], ['D', 'E'], ['F']]
            optimal_movements_5 = [('F', 'Table'), ('B', 'Table'), ('E', 'Table'), ('D', 'E'), ('C', 'Table'), ('B', 'C'), ('A', 'Table'), ('B', 'A'), ('C', 'Table'), ('A', 'C'), ('B', 'Table'), ('E', 'B')]
            return [initial_arrangement_5, goal_arrangement_5, optimal_movements_5]
        elif counter == 6:
            initial_arrangement_6 = [['D', 'F'], ['B', 'C'], ['A', 'E']]
            goal_arrangement_6 = [['A', 'B', 'C'], ['D', 'E'], ['F']]
            optimal_movements_6 = [('E', 'Table'), ('A', 'Table'), ('D', 'Table'), ('C', 'Table'), ('B', 'C'), ('A', 'Table'), ('B', 'A'), ('C', 'Table'), ('A', 'C'), ('D', 'Table'), ('C', 'D'), ('F', 'Table'), ('D', 'F')]
            return [initial_arrangement_6, goal_arrangement_6, optimal_movements_6]
        elif counter == 7:
            initial_arrangement_7 = [['C', 'A', 'D'], ['B', 'F'], ['E']]
            goal_arrangement_7 = [['A', 'B', 'C'], ['D', 'E'], ['F']]
            optimal_movements_7 = [('E', 'Table'), ('F', 'Table'), ('D', 'Table'), ('C', 'Table'), ('B', 'C'), ('A', 'Table'), ('B', 'A'), ('C', 'Table'), ('A', 'C'), ('D', 'Table'), ('C', 'D'), ('E', 'Table'), ('D', 'E'), ('F', 'Table')]
            return [initial_arrangement_7, goal_arrangement_7, optimal_movements_7]
        elif counter == 8:
            initial_arrangement_8 = [['F', 'B'], ['O', 'I', 'G', 'K'], ['N', 'L', 'J', 'P'], ['A', 'R', 'C'], ['B', 'E', 'D', 'Q'], ['H'], ['M']]
            goal_arrangement_8 = [['A', 'C', 'E'], ['F', 'I', 'M'], ['G', 'K'], ['L', 'N', 'P'], ['H', 'Q'], ['O'], ['R'], ['B', 'D', 'J']]
            optimal_movements_8 = [('F', 'Table'), ('B', 'Table'), ('O', 'Table'), ('I', 'O'), ('G', 'Table'), ('K', 'Table'), ('N', 'K'), ('L', 'N'), ('J', 'L'), ('P', 'J'), ('A', 'Table'), ('F', 'A'), ('R', 'Table'), ('F', 'R'), ('C', 'Table'), ('B', 'C'), ('E', 'B'), ('D', 'E'), ('Q', 'Table'), ('H', 'Table'), ('Q', 'H'), ('G', 'Table'), ('M', 'G'), ('I', 'M')]
            return [initial_arrangement_8, goal_arrangement_8, optimal_movements_8]
        elif counter == 9:
            initial_arrangement_9 = [['C', 'K', 'A', 'M', 'J', 'O', 'D', 'H'], ['L', 'E', 'N', 'G'], ['I', 'P'], ['F', 'B']]
            goal_arrangement_9 = [['M', 'K', 'L'], ['G', 'C'], ['E', 'A', 'O'], ['P', 'B', 'F', 'H', 'J', 'I', 'D', 'N']]
            optimal_movements_9 = [('C', 'Table'), ('K', 'Table'), ('A', 'Table'), ('M', 'Table'), ('J', 'Table'), ('O', 'Table'), ('D', 'Table'), ('H', 'Table'), ('L', 'Table'), ('E', 'Table'), ('N', 'Table'), ('G', 'Table'), ('I', 'Table'), ('P', 'Table'), ('F', 'Table'), ('B', 'Table')]
            return [initial_arrangement_9, goal_arrangement_9, optimal_movements_9]
        elif counter == 10:
            initial_arrangement_10 = [['B', 'C', 'D'], ['A', 'E'], ['F']]
            goal_arrangement_10 = [['A', 'B', 'C'], ['D', 'E'], ['F']]
            optimal_movements_10 = [('D', 'Table'), ('C', 'Table'), ('B', 'Table'), ('A', 'Table'), ('E', 'Table'), ('B', 'A'), ('C', 'B'), ('D', 'C')]
            return [initial_arrangement_10, goal_arrangement_10, optimal_movements_10]
        elif counter == 11:
            initial_arrangement_11 = [['E', 'F'], ['B', 'C'], ['A', 'D']]
            goal_arrangement_11 = [['A', 'B', 'C'], ['D', 'E'], ['F']]
            optimal_movements_11 = [('E', 'Table'), ('F', 'Table'), ('D', 'Table'), ('C', 'Table'), ('B', 'Table'), ('A', 'Table'), ('D', 'A'), ('C', 'D'), ('B', 'C'), ('E', 'Table'), ('B', 'E')]
            return [initial_arrangement_11, goal_arrangement_11, optimal_movements_11]
        elif counter == 12:
            initial_arrangement_12 = [['B', 'D', 'F'], ['C', 'E'], ['A']]
            goal_arrangement_12 = [['A', 'C', 'D'], ['B', 'E'], ['F']]
            optimal_movements_12 = [('C', 'Table'), ('B', 'Table'), ('D', 'Table'), ('A', 'Table'), ('E', 'Table'), ('F', 'Table'), ('D', 'C'), ('B', 'Table'), ('E', 'B'), ('D', 'Table'), ('C', 'D'), ('B', 'Table'), ('E', 'B')]
            return [initial_arrangement_12, goal_arrangement_12, optimal_movements_12]
        elif counter == 13:
            initial_arrangement_13 = [['B', 'D', 'F'], ['C', 'E'], ['A']]
            goal_arrangement_13 = [['A', 'C', 'D'], ['B', 'E'], ['F']]
            optimal_movements_13 = [('C', 'Table'), ('B', 'Table'), ('D', 'Table'), ('A', 'Table'), ('E', 'Table'), ('F', 'Table'), ('D', 'C'), ('B', 'Table'), ('E', 'B'), ('D', 'Table'), ('C', 'D'), ('B', 'Table'), ('E', 'B')]
            return [initial_arrangement_13, goal_arrangement_13, optimal_movements_13]
        elif counter == 14:
            initial_arrangement_14 = [['B', 'D', 'F'], ['C', 'E'], ['A']]
            goal_arrangement_14 = [['A', 'C', 'D'], ['B', 'E'], ['F']]
            optimal_movements_14 = [('C', 'Table'), ('B', 'Table'), ('D', 'Table'), ('A', 'Table'), ('E', 'Table'), ('F', 'Table'), ('D', 'C'), ('B', 'Table'), ('E', 'B'), ('D', 'Table'), ('C', 'D'), ('B', 'Table'), ('E', 'B')]
            return [initial_arrangement_14, goal_arrangement_14, optimal_movements_14]
        elif counter == 15:
            initial_arrangement_15 = [['B', 'D', 'F'], ['C', 'E'], ['A']]
            goal_arrangement_15 = [['A', 'C', 'D'], ['B', 'E'], ['F']]
            optimal_movements_15 = [('C', 'Table'), ('B', 'Table'), ('D', 'Table'), ('A', 'Table'), ('E', 'Table'), ('F', 'Table'), ('D', 'C'), ('B', 'Table'), ('E', 'B'), ('D', 'Table'), ('C', 'D'), ('B', 'Table'), ('E', 'B')]
            return [initial_arrangement_15, goal_arrangement_15, optimal_movements_15]
        else:
            return None

def main(args=None):
    rclpy.init(args=args)
    initial_goal_pub = InitialGoalPub()
    rclpy.spin(initial_goal_pub)
    initial_goal_pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
