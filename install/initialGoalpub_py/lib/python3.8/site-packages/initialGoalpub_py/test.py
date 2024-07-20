
def test():
    initial_arrangement_1  =  [['A', 'B', 'C'], ['D', 'E']]
    goal_arrangement_1  =  [['A', 'C'], ['D', 'E', 'B']]
    optimal_movements_1= [('C', 'Table'), ('B', 'E'), ('C', 'A')]

    initial_arrangement_2  =[['D', 'H', 'B', 'E'], ['G', 'A'], ['I', 'C', 'J', 'F']]
    goal_arrangement_2 = [['D', 'C'], ['G', 'E'], ['F', 'B', 'A', 'H'], ['J', 'I']]
    optimal_movements_2 =  [('A', 'Table'), ('E', 'G'), ('F', 'Table'), ('B', 'F'), ('A', 'B'), ('H', 'A'), ('J', 'Table'), ('C', 'D'), ('I', 'J')]

    initial_arrangement_3 = [['E', 'N', 'H', 'O'], ['L', 'F', 'K', 'B'], ['M', 'C'], ['A', 'I', 'J'], ['G', 'D']]
    goal_arrangement_3 = [['O', 'A', 'K', 'D', 'J', 'N'], ['I'], ['F', 'H', 'C'], ['E', 'L', 'M'], ['G', 'B']]
    optimal_movements_3  = [('J', 'Table'), ('I', 'Table'), ('O', 'Table'), ('A', 'O'), ('B', 'Table'), ('K', 'A'), ('D', 'K'), ('B', 'G'), ('J', 'D'), ('H', 'Table'), ('N', 'J'), ('F', 'Table'), ('L', 'E'), ('H', 'F'), ('C', 'H'), ('M', 'L')]

    initial_arrangement_4 = [['D', 'I'], ['J', 'K', 'E', 'A', 'H', 'C', 'G'], ['F', 'B']]
    goal_arrangement_4 = [['A', 'C', 'B'], ['G'], ['K'], ['F', 'H', 'I', 'E', 'J', 'D']]
    optimal_movements_4  = [('G', 'Table'), ('I', 'Table'), ('C', 'D'), ('B', 'C'), ('H', 'F'), ('I', 'H'), ('A', 'Table'), ('E', 'I'), ('K', 'Table'), ('J', 'E'), ('B', 'Table'), ('C', 'A'), ('D', 'J'), ('B', 'C')]

    initial_arrangement_5 = [['D', 'G', 'C', 'P', 'J', 'O', 'I', 'H'], ['A', 'Q', 'M', 'K'], ['L', 'F'], ['B', 'N', 'E']]
    goal_arrangement_5 = [['H', 'B'], ['E', 'P', 'D', 'K'], ['O', 'Q', 'G'], ['N', 'M', 'C'], ['F', 'I', 'J'], ['L', 'A']]
    optimal_movements_5  = [('H', 'Table'), ('F', 'Table'), ('I', 'F'), ('O', 'Table'), ('J', 'I'), ('E', 'Table'), ('P', 'E'), ('N', 'Table'), ('B', 'H'), ('K', 'Table'), ('M', 'N'), ('C', 'M'), ('G', 'Q'), ('D', 'P'), ('K', 'D'), ('G', 'Table'), ('Q', 'O'), ('A', 'L'), ('G', 'Q')]

    initial_arrangement_6 = [['F', 'B', 'C'], ['H', 'I'], ['M', 'E', 'J'], ['L', 'D', 'A', 'G', 'K']]
    goal_arrangement_6 = [['D', 'H', 'J', 'E', 'C'], ['L'], ['G', 'B', 'M'], ['I', 'A', 'F'], ['K']]
    optimal_movements_6  = [('K', 'Table'), ('C', 'Table'), ('G', 'Table'), ('B', 'G'), ('A', 'Table'), ('D', 'Table'), ('I', 'Table'), ('H', 'D'), ('J', 'H'), ('E', 'J'), ('M', 'B'), ('C', 'E'), ('A', 'I'), ('F', 'A')]

    initial_arrangement_7 = [['J', 'B', 'A', 'E', 'O', 'N'], ['I', 'G', 'K', 'P', 'Q', 'D', 'L', 'H'], ['F'], ['M', 'C']]
    goal_arrangement_7 = [['O', 'E', 'H', 'L'], ['A'], ['M', 'I', 'F'], ['B', 'K', 'G', 'N'], ['P'], ['J', 'Q', 'D'], ['C']]
    optimal_movements_7  = [('C', 'Table'), ('N', 'Table'), ('O', 'Table'), ('E', 'O'), ('A', 'Table'), ('H', 'E'), ('L', 'H'), ('B', 'Table'), ('D', 'Table'), ('Q', 'J'), ('D', 'Q'), ('P', 'Table'), ('K', 'B'), ('G', 'K'), ('N', 'G'), ('I', 'M'), ('F', 'I')]

    initial_arrangement_8 = [['O', 'B', 'D'], ['F', 'Q', 'I', 'P', 'A'], ['C', 'E', 'M', 'G'], ['R', 'N', 'L'], ['H', 'J'], ['K']]
    goal_arrangement_8 = [['M', 'G', 'I', 'O'], ['J', 'L', 'P'], ['H', 'Q', 'D', 'E', 'C', 'B'], ['N', 'K'], ['R', 'A', 'F']]
    optimal_movements_8  = [('J', 'Table'), ('L', 'J'), ('A', 'Table'), ('P', 'L'), ('I', 'Table'), ('Q', 'H'), ('D', 'Q'), ('N', 'Table'), ('K', 'N'), ('A', 'R'), ('F', 'A'), ('G', 'Table'), ('M', 'Table'), ('E', 'D'), ('C', 'E'), ('B', 'C'), ('G', 'M'), ('I', 'G'), ('O', 'I')]

    initial_arrangement_9 = [['C', 'B', 'F', 'O', 'D'], ['I', 'L', 'H', 'G', 'P', 'K', 'N'], ['J', 'E'], ['A', 'M']]
    goal_arrangement_9 = [['A', 'K'], ['C', 'G', 'F', 'O'], ['D', 'H', 'J'], ['B', 'I'], ['M', 'P'], ['E', 'L'], ['N']]
    optimal_movements_9  = [('N', 'Table'), ('M', 'Table'), ('K', 'A'), ('P', 'M'), ('D', 'Table'), ('G', 'Table'), ('H', 'D'), ('E', 'Table'), ('L', 'E'), ('J', 'H'), ('O', 'Table'), ('F', 'Table'), ('O', 'F'), ('B', 'Table'), ('I', 'B'), ('G', 'C'), ('O', 'Table'), ('F', 'G'), ('O', 'F')]

    initial_arrangement_10 = [['J', 'H', 'I', 'D', 'O', 'P', 'B', 'F', 'G', 'C', 'E', 'K', 'A'], ['Q', 'L'], ['N', 'M']]
    goal_arrangement_10 = [['P', 'N', 'H', 'C'], ['O', 'K', 'Q', 'J', 'D', 'B', 'I'], ['M', 'E', 'A'], ['G', 'L'], ['F']]
    optimal_movements_10  = [('A', 'Table'), ('K', 'Table'), ('M', 'Table'), ('E', 'M'), ('A', 'E'), ('C', 'Table'), ('G', 'Table'), ('L', 'G'), ('F', 'Table'), ('B', 'Table'), ('P', 'Table'), ('N', 'P'), ('O', 'Table'), ('K', 'O'), ('Q', 'K'), ('D', 'Table'), ('I', 'Table'), ('H', 'N'), ('C', 'H'), ('J', 'Q'), ('D', 'J'), ('B', 'D'), ('I', 'B')]

    initial_arrangement_11 = [['A', 'B', 'C'], ['D', 'E']]
    goal_arrangement_11 = [['D', 'E', 'A', 'B', 'C']]
    optimal_movements_11 = [('C', 'Table'), ('B', 'Table'), ('A', 'E'), ('B', 'A'), ('C', 'B')]

    initial_arrangement_12 = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
    goal_arrangement_12 = [['I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']]
    optimal_movements_12  = [('I', 'Table'), ('H', 'I'), ('G', 'H'), ('F', 'G'), ('E', 'F'), ('D', 'E'), ('C', 'D'), ('B', 'C'), ('A', 'B')]

    initial_arrangement_13 = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
    goal_arrangement_13 = [['F', 'D', 'C', 'I', 'G', 'A'], ['B', 'E', 'H']]
    optimal_movements_13  = [('F', 'Table'), ('E', 'Table'), ('D', 'F'), ('C', 'D'), ('I', 'C'), ('B', 'Table'), ('E', 'B'), ('H', 'Table'), ('H', 'E'), ('G', 'I'), ('A', 'G')]

if __name__ == "__main__":
    test()