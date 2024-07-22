#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_set>
#include <algorithm>
#include <sstream>
// #include "BlockArrangmentAlgorithm.hpp"
// #include "../include/CPPsub_BlocksRearrange/BlockArrangmentAlgorithm.hpp"

#include "../include/CPPsub_BlocksRearrange/StateSpace.h"

/*==========================================================================*/
/*============================ StateSpace class ============================*/
/*==========================================================================*/

StateSpace::StateSpace() : state({}), move({}), fixedCount(0) {}
StateSpace::StateSpace(State s) : state(s), move({}), fixedCount(0) {}
StateSpace::StateSpace(State s, Moves m) : state(s), move(m), fixedCount(0) {}
StateSpace::StateSpace(State s, Moves m, int f) : state(s), move(m), fixedCount(f) {}

// StateSpace setters (simple setters / no chaecks or validations needed)
void StateSpace::setState(State s) { state = s; };
void StateSpace::setMoves(Moves m) { move = m; };
void StateSpace::setFixedCount(int f) { fixedCount = f; };
void StateSpace::setBlockGoal(int x, int y) { state[x][y].isgoal = true; };

// StateSpace getters
State StateSpace::getState() const { return state; };
Moves StateSpace::getMoves() const { return move; };
int StateSpace::getFixedCount() const { return fixedCount; };

// operator overloading for the priority queue comparison (for max heap)
bool StateSpace::operator<(const StateSpace &other) const
{
     return (fixedCount) < (other.getFixedCount());
};
