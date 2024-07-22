import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class initialGoalPub(Node):
    def __init__(self):
        super().__init__("initGoalPub")
        self.publisher_ = self.create_publisher(String, "initGoalTopic", 13)
        time_period = 1
        self.timer = self.create_timer(time_period, self.timer_callback)
        self.counter = 1
        self.max_test_cases = 13  # Set the maximum number of test cases
        self.all_published = False

    def timer_callback(self):
        msg = String()
        data = self.get_test_cases()
        if data is not None:
            initial_goal_optimal = data
            combined_str = self.lists_to_string(initial_goal_optimal)
            msg.data = combined_str
            self.publisher_.publish(msg)   # the msg sent is i,n/p,u/t|g,o/a,L|s,o/l
            self.get_logger().info(f"publishing: {msg}")
            self.counter += 1
        else:
            self.get_logger().info('All test cases published, shutting down.')
            self.all_published = True
            
    def get_test_cases(self):
        all = self.get_initial_goal_optimal()
        combined_str = self.lists_to_string(all)
        return combined_str

    def lists_to_string(self, all, section_delim="|", row_delim="/", col_delim=","):
        def list_to_string(lst):
            return row_delim.join([col_delim.join(row) for row in lst])
        list1_str = list_to_string(all[0])
        list2_str = list_to_string(all[1])
        list3_str = row_delim.join([col_delim.join(pair) for pair in all[2]])
        combined_str = section_delim.join([list1_str, list2_str, list3_str])
        return combined_str            

    def get_test_cases(self):  # 13 test cases
        counter = self.counter
        if counter ==1:
            initial_arrangement_1  =  [['A', 'B', 'C'], ['D', 'E']]
            goal_arrangement_1  =  [['A', 'C'], ['D', 'E', 'B']]
            optimal_movements_1= [('C', 'Table'), ('B', 'E'), ('C', 'A')]
            return [initial_arrangement_1, goal_arrangement_1, optimal_movements_1]
        elif counter == 2:
            initial_arrangement_2  =[['D', 'H', 'B', 'E'], ['G', 'A'], ['I', 'C', 'J', 'F']]
            goal_arrangement_2 = [['D', 'C'], ['G', 'E'], ['F', 'B', 'A', 'H'], ['J', 'I']]
            optimal_movements_2 =  [('A', 'Table'), ('E', 'G'), ('F', 'Table'), ('B', 'F'), ('A', 'B'), ('H', 'A'), ('J', 'Table'), ('C', 'D'), ('I', 'J')]
            return [initial_arrangement_2, goal_arrangement_2, optimal_movements_2]
        elif counter ==3:
            initial_arrangement_3 = [['E', 'N', 'H', 'O'], ['L', 'F', 'K', 'B'], ['M', 'C'], ['A', 'I', 'J'], ['G', 'D']]
            goal_arrangement_3 = [['O', 'A', 'K', 'D', 'J', 'N'], ['I'], ['F', 'H', 'C'], ['E', 'L', 'M'], ['G', 'B']]
            optimal_movements_3  = [('J', 'Table'), ('I', 'Table'), ('O', 'Table'), ('A', 'O'), ('B', 'Table'), ('K', 'A'), ('D', 'K'), ('B', 'G'), ('J', 'D'), ('H', 'Table'), ('N', 'J'), ('F', 'Table'), ('L', 'E'), ('H', 'F'), ('C', 'H'), ('M', 'L')]
            return [initial_arrangement_3, goal_arrangement_3, optimal_movements_3]
        elif counter == 4:
            initial_arrangement_4 = [['D', 'I'], ['J', 'K', 'E', 'A', 'H', 'C', 'G'], ['F', 'B']]
            goal_arrangement_4 = [['A', 'C', 'B'], ['G'], ['K'], ['F', 'H', 'I', 'E', 'J', 'D']]
            optimal_movements_4  = [('G', 'Table'), ('I', 'Table'), ('C', 'D'), ('B', 'C'), ('H', 'F'), ('I', 'H'), ('A', 'Table'), ('E', 'I'), ('K', 'Table'), ('J', 'E'), ('B', 'Table'), ('C', 'A'), ('D', 'J'), ('B', 'C')]
            return [initial_arrangement_4, goal_arrangement_4, optimal_movements_4]
        elif counter == 5:
            initial_arrangement_5 = [['D', 'G', 'C', 'P', 'J', 'O', 'I', 'H'], ['A', 'Q', 'M', 'K'], ['L', 'F'], ['B', 'N', 'E']]
            goal_arrangement_5 = [['H', 'B'], ['E', 'P', 'D', 'K'], ['O', 'Q', 'G'], ['N', 'M', 'C'], ['F', 'I', 'J'], ['L', 'A']]
            optimal_movements_5  = [('H', 'Table'), ('F', 'Table'), ('I', 'F'), ('O', 'Table'), ('J', 'I'), ('E', 'Table'), ('P', 'E'), ('N', 'Table'), ('B', 'H'), ('K', 'Table'), ('M', 'N'), ('C', 'M'), ('G', 'Q'), ('D', 'P'), ('K', 'D'), ('G', 'Table'), ('Q', 'O'), ('A', 'L'), ('G', 'Q')]
            return [initial_arrangement_5, goal_arrangement_5, optimal_movements_5]
        elif counter == 6:
            initial_arrangement_6 = [['F', 'B', 'C'], ['H', 'I'], ['M', 'E', 'J'], ['L', 'D', 'A', 'G', 'K']]
            goal_arrangement_6 = [['D', 'H', 'J', 'E', 'C'], ['L'], ['G', 'B', 'M'], ['I', 'A', 'F'], ['K']]
            optimal_movements_6  = [('K', 'Table'), ('C', 'Table'), ('G', 'Table'), ('B', 'G'), ('A', 'Table'), ('D', 'Table'), ('I', 'Table'), ('H', 'D'), ('J', 'H'), ('E', 'J'), ('M', 'B'), ('C', 'E'), ('A', 'I'), ('F', 'A')]
            return [initial_arrangement_6, goal_arrangement_6, optimal_movements_6]
        elif counter == 7:
            initial_arrangement_7 = [['J', 'B', 'A', 'E', 'O', 'N'], ['I', 'G', 'K', 'P', 'Q', 'D', 'L', 'H'], ['F'], ['M', 'C']]
            goal_arrangement_7 = [['O', 'E', 'H', 'L'], ['A'], ['M', 'I', 'F'], ['B', 'K', 'G', 'N'], ['P'], ['J', 'Q', 'D'], ['C']]
            optimal_movements_7  = [('C', 'Table'), ('N', 'Table'), ('O', 'Table'), ('E', 'O'), ('A', 'Table'), ('H', 'E'), ('L', 'H'), ('B', 'Table'), ('D', 'Table'), ('Q', 'J'), ('D', 'Q'), ('P', 'Table'), ('K', 'B'), ('G', 'K'), ('N', 'G'), ('I', 'M'), ('F', 'I')]
            return [initial_arrangement_7, goal_arrangement_7, optimal_movements_7]
        elif counter == 8:
            initial_arrangement_8 = [['O', 'B', 'D'], ['F', 'Q', 'I', 'P', 'A'], ['C', 'E', 'M', 'G'], ['R', 'N', 'L'], ['H', 'J'], ['K']]
            goal_arrangement_8 = [['M', 'G', 'I', 'O'], ['J', 'L', 'P'], ['H', 'Q', 'D', 'E', 'C', 'B'], ['N', 'K'], ['R', 'A', 'F']]
            optimal_movements_8  = [('J', 'Table'), ('L', 'J'), ('A', 'Table'), ('P', 'L'), ('I', 'Table'), ('Q', 'H'), ('D', 'Q'), ('N', 'Table'), ('K', 'N'), ('A', 'R'), ('F', 'A'), ('G', 'Table'), ('M', 'Table'), ('E', 'D'), ('C', 'E'), ('B', 'C'), ('G', 'M'), ('I', 'G'), ('O', 'I')]
            return [initial_arrangement_8, goal_arrangement_8, optimal_movements_8]
        elif counter == 9:
            initial_arrangement_9 = [['C', 'B', 'F', 'O', 'D'], ['I', 'L', 'H', 'G', 'P', 'K', 'N'], ['J', 'E'], ['A', 'M']]
            goal_arrangement_9 = [['A', 'K'], ['C', 'G', 'F', 'O'], ['D', 'H', 'J'], ['B', 'I'], ['M', 'P'], ['E', 'L'], ['N']]
            optimal_movements_9  = [('N', 'Table'), ('M', 'Table'), ('K', 'A'), ('P', 'M'), ('D', 'Table'), ('G', 'Table'), ('H', 'D'), ('E', 'Table'), ('L', 'E'), ('J', 'H'), ('O', 'Table'), ('F', 'Table'), ('O', 'F'), ('B', 'Table'), ('I', 'B'), ('G', 'C'), ('O', 'Table'), ('F', 'G'), ('O', 'F')]
            return [initial_arrangement_9, goal_arrangement_9, optimal_movements_9]
        elif counter == 10:
            initial_arrangement_10 = [['J', 'H', 'I', 'D', 'O', 'P', 'B', 'F', 'G', 'C', 'E', 'K', 'A'], ['Q', 'L'], ['N', 'M']]
            goal_arrangement_10 = [['P', 'N', 'H', 'C'], ['O', 'K', 'Q', 'J', 'D', 'B', 'I'], ['M', 'E', 'A'], ['G', 'L'], ['F']]
            optimal_movements_10  = [('A', 'Table'), ('K', 'Table'), ('M', 'Table'), ('E', 'M'), ('A', 'E'), ('C', 'Table'), ('G', 'Table'), ('L', 'G'), ('F', 'Table'), ('B', 'Table'), ('P', 'Table'), ('N', 'P'), ('O', 'Table'), ('K', 'O'), ('Q', 'K'), ('D', 'Table'), ('I', 'Table'), ('H', 'N'), ('C', 'H'), ('J', 'Q'), ('D', 'J'), ('B', 'D'), ('I', 'B')]
            return [initial_arrangement_10, goal_arrangement_10, optimal_movements_10]
        elif counter == 11:
            initial_arrangement_11 = [['A', 'B', 'C'], ['D', 'E']]
            goal_arrangement_11 = [['D', 'E', 'A', 'B', 'C']]
            optimal_movements_11 = [('C', 'Table'), ('B', 'Table'), ('A', 'E'), ('B', 'A'), ('C', 'B')]
            return [initial_arrangement_11, goal_arrangement_11, optimal_movements_11]
        elif counter == 12:
            initial_arrangement_12 = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
            goal_arrangement_12 = [['I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']]
            optimal_movements_12  = [('I', 'Table'), ('H', 'I'), ('G', 'H'), ('F', 'G'), ('E', 'F'), ('D', 'E'), ('C', 'D'), ('B', 'C'), ('A', 'B')]
            return [initial_arrangement_12, goal_arrangement_12, optimal_movements_12]
        elif counter == 13:
            initial_arrangement_13 = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
            goal_arrangement_13 = [['F', 'D', 'C', 'I', 'G', 'A'], ['B', 'E', 'H']]
            optimal_movements_13  = [('F', 'Table'), ('E', 'Table'), ('D', 'F'), ('C', 'D'), ('I', 'C'), ('B', 'Table'), ('E', 'B'), ('H', 'Table'), ('H', 'E'), ('G', 'I'), ('A', 'G')]
            return [initial_arrangement_13, goal_arrangement_13, optimal_movements_13]
        else:
            return None
        
def main(args=None):
    rclpy.init(args=args)
    initial_goal_pub = initialGoalPub()
    executor = rclpy.executors.SingleThreadedExecutor()
    executor.add_node(initial_goal_pub)
    
    # terminate the after publishing all test cases
    while rclpy.ok() and not initial_goal_pub.all_published:
        executor.spin_once(timeout_sec=0.1)
    
    initial_goal_pub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()