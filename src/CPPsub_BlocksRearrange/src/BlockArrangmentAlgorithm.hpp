#ifndef BlockArrangmentAlgorithm_HPP
#define BlockArrangmentAlgorithm_HPP

#include <vector>
using namespace std;

struct Block
{
     char letter;
     bool isgoal;

     Block(char let) : letter(let), isgoal(0){};
};

// type aliases
using State = vector<vector<Block>>;        // 2D vector to store the stacks of blocks
using Moves = vector<pair<string, string>>; // pair of block and its destination


/*==========================================================================*/
/*============================ StateSpace class ============================*/
/*==========================================================================*/

class StateSpace
{
     State state;
     Moves move;
     int fixedCount; // how close you are to the goal

public:
     // constructors
     StateSpace() {}
     StateSpace(State s) {}
     StateSpace(State s, Moves m) {}
     StateSpace(State s, Moves m, int f) {}

     // setters for the attributes
     void setState(State s) {};
     void setMoves(Moves m) {};
     void setFixedCount(int f) {};

     // getters for the attributes
     State getState() const {};
     Moves getMoves() const {};
     int getFixedCount() const {};

     // operator overloading for the priority queue comparison (for max heap)
     bool operator<(const StateSpace &other) const {};
};


/*==========================================================================*/
/*=========================== BFSAlgorithm class ===========================*/
/*==========================================================================*/

class BFSAlgorithm
{
     State initial;
     State goal;
     Moves optimalMoves; // for comparison only
     Moves path;

public:
     // constructor to decompresses publisher's msg of initial,
     // goal. and sol to 2D vectors and initializes the algorithm
     BFSAlgorithm(string pub_msg) {}

     // function to convert compressed states string to vector again (the publisher msg of initial, goal, and sol to 2D vectors)
     vector<string> StringToVector(string pub_msg, char delim) {}

     // function to convert the state vector to string representation for easy comparisons
     string VectorToString(const State &state) const {}

     // function to check if goal is reached
     bool IsGoal(const State &current, const State &goal) const {}

     // function to generate the next possible states from a current state
     vector<StateSpace> getNextStates(const StateSpace &current) const {}

     // function to count blocks in goal pos and update state's fixedCount attribute
     void countMatches(StateSpace &current, const State &goal) {}

     // BFS algorithm to find the optimal path to reach the goal state
     Moves BFS_Algorithm(const State &start, const State &goal) {}

};

#endif // BlockArrangmentAlgorithm_HPP