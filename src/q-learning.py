from tkinter import *
from src.data import *

q = {}
current_state_i, current_state_j = start_position_i, start_position_j


# possible action from given status (i, j)
def possible_actions(i, j):
    act_list = []
    for action in actions.items():
        ii, jj = i + action[1][0], j + action[1][1]
        if 0 <= ii < len(states) and 0 <= jj < len(states[i]):
            act_list.append(action[0])
    return act_list


# initialize Q function with zeros
def initialize_q():
    for i in range(0, len(states)):
        for j in range(0, len(states[i])):
            for action in possible_actions(i, j):
                q[(i, j, action)] = 0


# reward function
def compute_reward(next_i, next_j):
    return rewards[states[next_i][next_j]]


# action choose policy (here best action is the one with immediately best reward or least penalty)
def best_action_policy(ii, jj):
    max_act = max(possible_actions(ii, jj), key=lambda possible_action: q[(ii, jj, possible_action)])
    return max_act


# take the given action and returns new status
def take_action(i, j, action):
    return i + actions[action][0], j + actions[action][1]


# Q-update function
def q_update(i, j, action, next_i, next_j):
    reward = compute_reward(next_i, next_j)
    return (1 - alpha) * q[(i, j, action)] + alpha * (
            reward + gamma * q[(next_i, next_j, best_action_policy(next_i, next_j))])


# the q-learning algorithm
def q_learning(i, j):
    for act in possible_actions(i, j):
        ii, jj = take_action(i, j, act)
        q[(i, j, act)] = q_update(i, j, act, ii, jj)
    best_act = best_action_policy(i, j)
    ii, jj = take_action(i, j, best_act)
    print('old status : (', i, j, ') -', best_act, '- new state : (', ii, jj, ')')
    return ii, jj


#
def game():
    # next iteration of Q-Learning algorithm
    global current_state_i, current_state_j, q
    current_state_i, current_state_j = q_learning(current_state_i, current_state_j)
    # update game visual with new status from q_learning
    canvas.delete(ALL)
    nb_cells_ver = len(states)
    for i in range(0, nb_cells_ver):
        nb_cells_hor = len(states[i])
        cell_width = width / nb_cells_hor
        cell_height = height / nb_cells_ver
        for j in range(0, nb_cells_hor):
            canvas.create_rectangle(cell_width * j, cell_height * i, cell_width * (j + 1), cell_height * (i + 1),
                                    fill=colors[(states[i][j])])
            if i == current_state_i and j == current_state_j:
                canvas.create_oval(cell_width * j, cell_height * i, cell_width * (j + 1), cell_height * (i + 1),
                                   fill=agent_color)
    canvas.after(step_wait_time, game)


# initialize Q function
initialize_q()

# Launch the app
window = Tk()
window.title(title)
window.geometry(str(width) + "x" + str(height))
canvas = Canvas(window, width=width, height=height, borderwidth=0, highlightthickness=0)
canvas.pack()
canvas.after(0, game)
window.mainloop()
