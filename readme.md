### Q-Learning algorithm
#### Présentation
Reinforcement learning, one of the most active research areas in artificial intelligence, is a computational approach to learning whereby an agent tries to maximize the total amount of reward it receives when interacting with a complex, uncertain environment.
#### Algorithm
Given a set of states and actions, Ql-learning algorithm is based on continuous update (learning) of a function Q.
For each taken action agent receives a reward (or penalty) and updates the Q function.
The goal of the agent is to maximise the reward.
```
Q[s, a] = Q[s, a] + alpha*(R + gamma*Max[Q(s’, a’)] - Q[s, a])
```
where : 
- s : is a any state from envirement.
- a : is any action that can be taken from a given state
- Q : value function for each state-action couple.
- alpha : (between 0 and 1) is the learning rate, indicates how much new calculated information is important compared to older information. when 0, agent doesn't learn, when 1, agent ignores what it already learned
- gamma : eagerness, determines how much future rewards are important, when close to 0, agent gives more considerations to current rewards, when close to 1, agent considers more future rewards when updating Q.

#### Pseudo Code
```
Q-Learning :
    Initialize Q-values (Q(s,a)) arbitrarily for all state-action pairs.
    Repeat while learning
        Choose an action (a) in the current world state (s) based on current Q-value estimates (Q(s,⋅)).
        Take the action (a) and observe the the outcome state (s′) and reward (r).
        Q[s, a] = Q[s, a] + alpha*(R + gamma*Max[Q(s’, a')] - Q[s, a])
```
#### Run
```
python q-learning.py
``` 

### Example
In our example here, the agent searches a door to go out of the Maze.
To achieve this goal, agent explores the maze and updates it's Q functions.
##### States and rewards
- R: Road penalty is agent stays in road (-1 penalty will force agent to move).
- H: Hole penalty if agent falls in mud hole (-5 penalty).
- W: Water penalty if agent falls in water (-100 penalty).
- G: Goal reward if agent achieves its mission (+100 reward).
##### Actions : 
- UP
- DOWN
- LEFT
- RIGHT

##### Grid
![Game](/q-learning-maze.png)