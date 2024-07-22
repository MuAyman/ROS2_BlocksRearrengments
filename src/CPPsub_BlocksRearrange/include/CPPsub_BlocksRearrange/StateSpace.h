#ifndef StateSpace_H
#define StateSpace_H

#include <vector>
#include <string>
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
     StateSpace();
     StateSpace(State s);
     StateSpace(State s, Moves m);
     StateSpace(State s, Moves m, int f);

     // setters for the attributes
     void setState(State s);
     void setMoves(Moves m);
     void setFixedCount(int f);
     void setBlockGoal(int x, int y);

     // getters for the attributes
     State getState() const;
     Moves getMoves() const;
     int getFixedCount() const;

     // operator overloading for the priority queue comparison (for max heap)
     bool operator<(const StateSpace &other) const;
};

#endif // StateSpace_H