#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_set>
#include <algorithm>
#include <sstream>

#include "../include/CPPsub_BlocksRearrange/BFSAlgorithm.h"
#include "../include/CPPsub_BlocksRearrange/StateSpace.h"

using namespace std;
/*==========================================================================*/
/*=========================== BFSAlgorithm class ===========================*/
/*==========================================================================*/

// initialize the static member testNum
int BFSAlgorithm::testNum = 0;

// constructor to decompresses publisher's msg of initial,
// goal. and sol to 2D vectors
BFSAlgorithm::BFSAlgorithm(string pub_msg)
{
	path = {};									 // intialize path with empty path
	++testNum;									 // counting the number of the test for the display (compare function)
	vector<string> allThree = StringToVector(pub_msg, '|'); // [init, goal, sol]
	// Deserialize initial and goal vector (both of type State)
	for (int i = 0; i < 2; ++i)
	{
		vector<string> Stacks = StringToVector(allThree[i], '/'); // Stacks = [stack1/stack2...etc]
		for (const auto &stack : Stacks)
		{
			vector<string> letters = StringToVector(stack, ','); // letters = ["A", "B", "C",...etc]
			vector<Block> blocks;
			for (const auto &letter : letters) // converting from string to Block
				blocks.push_back(letter[0]);
			if (i == 0) // initial
				initial.push_back(blocks);
			else // goal
				goal.push_back(blocks);
		}
	}

	// Deserialize sol vector (of type Moves)
	vector<string> solPairs = StringToVector(allThree[2], '/');
	for (const auto &pair : solPairs)
	{
		vector<string> elements = StringToVector(pair, ','); // elements = ["A", "Table", "B", "C", ...etc]
		optimalMoves.push_back({elements[0], elements[1]});
	}
}

// function to convert compressed states strings to vectors
// (publisher msg of initial, goal, and sol to 2D vectors)
vector<string> BFSAlgorithm::StringToVector(string pub_msg, char delim)
{
	vector<string> strVector;
	stringstream ss(pub_msg);
	string str;
	while (getline(ss, str, delim))
		strVector.push_back(str);
	return strVector;
};

// function to compress state vectors to strings (with sorted stacks meaning
// if state = DB/AC is will be AC/DB (same block congiuration but sorted to prevent repetition
string BFSAlgorithm::VectorToString(const State &state) const
{
	State s = state; // to store sorted state
	bool swapped = 0;
	// bubble sort for the stacks of state (to insure AD/BC is same as BC/AD)
	for (int i = 0; i < s.size() - 1; ++i)
	{
		swapped = 0;
		for (int j = 0; j < s.size() - i - 1; ++j)
		{
			if (s[j + 1].empty()) // moving empty states to the end of the state vector
				continue;
			else if (s[j].empty()) // moving empty states to the end of the state vector
			{
				swap(s[j], s[j + 1]); // swaping the two stacks of the state vector
				swapped = 1;
			}
			else if (s[j][0].letter > s[j + 1][0].letter) // comparing the tables (elements on the table) and sorting accourrding to them
			{
				swap(s[j], s[j + 1]); // swaping the two stacks of the state vector
				swapped = 1;
			}
		}
		if (!swapped)
			break; // already sorted
	}

	// now to convert the sorted state vector so now AB/BC is same as BC/AD (avoid reapting states)
	string wholeState;
	for (const auto &stack : s) // avoid copying stacks + not changing it
	{
		for (auto blocks : stack)
			wholeState += blocks.letter;
		wholeState += "/"; // separate stacks from each other
	}
	return wholeState;
};

// function to check if goal is reached
bool BFSAlgorithm::IsGoal(const State &current) const
{
	int flag = 0, totalBloacksNum = 0; // to count the num of similar Stacks
	for (const auto &curStack : current)
	{
		totalBloacksNum += curStack.size(); // counting the total num of letters
		for (const auto &blocks : curStack)
			if (blocks.isgoal) // conting the num of blocks in goal pos
				++flag;
	}

	if (flag == totalBloacksNum)
		return true; // goal reached if all blocks are in goal pos
	else
		return false;
};

// function to generate the next possible states from a current state
vector<StateSpace> BFSAlgorithm::getNextStates(const StateSpace &current) const
{
	vector<StateSpace> nextStates;

	for (int i = 0; i < current.getState().size(); ++i)
	{
		if (!current.getState()[i].empty())
		{ // Current stack not empty
			Block topBlock = current.getState()[i].back();

			// moving the top blocks of one stack to another stack
			for (int j = 0; j < current.getState().size(); ++j)
			{
				if (i != j)
				{ // check that its a different stack
					State newState = current.getState();
					int newFixed = current.getFixedCount();
					Moves newPath = current.getMoves();
					newPath.push_back(make_pair(string(1, topBlock.letter), current.getState()[j].empty() ? "Table" : string(1, current.getState()[j].back().letter)));
					newState[j].push_back(topBlock);
					newState[i].pop_back();
					nextStates.push_back({newState, newPath, newFixed});
				}
			}
			// moving the top blocks to an existing empty stack before adding new stack
			bool emptyStackUsed = false;
			for (int j = 0; j < current.getState().size(); ++j)
			{
				if (current.getState()[j].empty())
				{ // if you found an empty stack already, use it
					State newState = current.getState();
					int newFixed = current.getFixedCount();
					Moves newPath = current.getMoves();
					newState[j].push_back({topBlock}); // push back in the empty stack
					newPath.push_back(make_pair(string(1, topBlock.letter), "Table"));
					newState[i].pop_back();
					nextStates.push_back({newState, newPath, newFixed});
					emptyStackUsed = true;
					break;
				}
			}
			// if no empty stack found, create a new stack
			if (!emptyStackUsed)
			{
				State newState = current.getState();
				int newFixed = current.getFixedCount();
				Moves newPath = current.getMoves();
				newState.push_back({topBlock});
				newPath.push_back(make_pair(string(1, topBlock.letter), "Table"));
				newState[i].pop_back();
				nextStates.push_back({newState, newPath, newFixed});
			}
		}
	}
	return nextStates;
};

// function to count blocks in goal pos and update state's fixedCount attribute
void BFSAlgorithm::countMatches(StateSpace &current)
{
	current.setFixedCount(0); // insuring it hasnt been counted before so that we double the count
	// check if any of the tables (blocks on table) are in the right place
	int i = 0;
	for (auto &curStack : current.getState())
	{ // without const as we are marking the DONE letters
		if (!curStack.empty())
		{
			for (const auto &goalStack : goal)
			{
				if (curStack.front().letter == goalStack.front().letter)
				{
					current.setBlockGoal(i, 0); // setting the first element of curStack to be in goal pos
					curStack[0].isgoal = true;  // marking the matched element that it is fixed and not to be moved
					int f = (current.getFixedCount());
					current.setFixedCount(++f);
					int counter = 0;																			   // to iterate over the rest of the stack
					while (current.getState()[i][counter].isgoal && counter < curStack.size() - 1 && counter < goalStack.size() - 1) // extend the checking to the elements above
					{																						   // making sure that the counter doesnt go beyond the current or goal Stacks
						++counter;
						if (curStack[counter].letter == goalStack[counter].letter)
						{
							current.setBlockGoal(i, counter);
							curStack[counter].isgoal = true; // mark done
							int f = current.getFixedCount();
							current.setFixedCount(++f);
						}
					}
				}
			}
		}
		++i;
	}
};

// BFS algorithm to find the optimal path to reach the goal state
Moves BFSAlgorithm::BFS_Algorithm()
{
	priority_queue<StateSpace> BFSq; // priority queue to prioritize the states nearer to the goal
	unordered_set<string> visited;   // set -> to prevent repeated states, unordered -> to enhance the search efficacy
	BFSq.push(initial);
	visited.insert(VectorToString(initial)); // store the visited states as a string for ease of access and comparison

	while (!BFSq.empty())
	{
		StateSpace current(BFSq.top());
		BFSq.pop();
		if (IsGoal(current.getState()))
		{
			path = current.getMoves();
			return path;
		}
		countMatches(current);							 // count the num of letters in goal pos to use in the priority queue
		visited.insert(VectorToString(current.getState()));	 // update the visited states
		vector<StateSpace> nextStates = getNextStates(current); // getting the next possible states from the current one to discover
		for (auto &nextState : nextStates)					 // looping on them to check if visited before and count the matches
		{
			string stateString = VectorToString(nextState.getState());
			if (visited.find(stateString) == visited.end())
			{ // check if visited before
				countMatches(nextState);
				BFSq.push(nextState);
			}
		}
	}
	return {}; // return empty path if no path is found
};

// function to comapre the path reached with the provided optimal path
void BFSAlgorithm::compare()
{
	// Your comparison logic
	cout << "\n============== VSCODE ===================";
	cout << "\nTest num: " << testNum;
	cout << "\n\tmy Sol moves: " << path.size()
		<< "\n\t  Test moves: " << optimalMoves.size() << "\n";
	cout << "The moves: ";
	for (const auto &pair : path)
		cout << "(" << pair.first << ", " << pair.second << "), ";
	cout << "\n============== VSCODE ===================\n";
}