#ifndef BFSAlgorithm_H
#define BFSAlgorithm_H

// #include <vector>
// #include <string>
using namespace std;

#include "StateSpace.h"

/*==========================================================================*/
/*=========================== BFSAlgorithm class ===========================*/
/*==========================================================================*/

class BFSAlgorithm
{
public:
     State initial;
     State goal;
     Moves optimalMoves; // for comparison only
     Moves path;
     static int testNum;

     // constructor to decompresses publisher's msg of initial,
     // goal. and sol to 2D vectors and initializes the algorithm
     BFSAlgorithm(string pub_msg);

     // function to convert compressed states string to vector again (the publisher msg of initial, goal, and sol to 2D vectors)
     vector<string> StringToVector(string pub_msg, char delim);

     // function to convert the state vector to string representation for easy comparisons
     string VectorToString(const State &state) const;

     // function to check if goal is reached
     bool IsGoal(const State &current) const;

     // function to generate the next possible states from a current state
     vector<StateSpace> getNextStates(const StateSpace &current) const;

     // function to count blocks in goal pos and update state's fixedCount attribute
     void countMatches(StateSpace &current);

     // BFS algorithm to find the optimal path to reach the goal state
     Moves BFS_Algorithm();

     // function to comapre the path reached with the provided optimal path
     void compare();
};

#endif // BFSAlgorithm_H