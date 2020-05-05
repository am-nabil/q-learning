from tkinter import *

states = [
    ['R', 'W', 'R', 'R', 'W', 'R', 'R', 'R'],
    ['R', 'H', 'R', 'R', 'W', 'R', 'R', 'R'],
    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
    ['W', 'W', 'R', 'R', 'R', 'W', 'R', 'R'],
    ['W', 'W', 'W', 'W', 'R', 'W', 'R', 'R'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'R', 'R'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'R', 'R'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'R', 'H'],
    ['W', 'W', 'R', 'R', 'R', 'R', 'R', 'R'],
    ['R', 'R', 'R', 'R', 'R', 'R', 'H', 'G']
]

rewards = {
    'R': -1,
    'H': -5,
    'W': -100,
    'G': +100
}

actions = {
    'UP': (-1, 0),
    'DOWN': (+1, 0),
    'RIGHT': (0, +1),
    'LEFT': (0, -1),
    'STAY': (0, 0)
}

q = {}
current_state_i, current_state_j = 0, 0
alpha = 0.1  # learning rate
gamma = 0.9  # Eagerness


def possibleActions(i, j):
    act_list = []
    for action in actions.items():
        ii, jj = i + action[1][0], j + action[1][1]
        if 0 <= ii < len(states) and 0 <= jj < len(states[i]):
            act_list.append(action[0])
    return act_list


def initializeQ():
    for i in range(0, len(states)):
        for j in range(0, len(states[i])):
            for action in possibleActions(i, j):
                q[(i, j, action)] = 0


def Q(i, j, action, next_i, next_j):
    reward = compute_reward(next_i, next_j)
    return (1 - alpha) * q[(i, j, action)] + alpha * (
            reward + gamma * q[(next_i, next_j, best_action_policy(next_i, next_j, q))])


def compute_reward(next_i, next_j):
    return rewards[states[next_i][next_j]]


def best_action_policy(ii, jj, q_function):
    max_act = max(possibleActions(ii, jj), key=lambda possible_action: q_function[(ii, jj, possible_action)])
    return max_act


def take_action(i, j, action):
    return i + actions[action][0], j + actions[action][1]


def learnQ(i, j, q_function):
    for act in possibleActions(i, j):
        ii, jj = take_action(i, j, act)
        q_function[(i, j, act)] = round(Q(i, j, act, ii, jj), 2)
    best_act = best_action_policy(i, j, q_function)
    ii, jj = take_action(i, j, best_act)
    print('old status : (', i, j, ') -', best_act, '- new state : (', ii, jj, ')')
    return ii, jj, q_function


def get_color(state):
    colors = {"W": "#1ae5ef", "H": "#c96134", "R": "#7e9296", "G": "#2ccc44"}
    return colors[state]


def game():
    # next iteration of Q-Learning algorithm
    global current_state_i, current_state_j, q
    current_state_i, current_state_j, q = learnQ(current_state_i, current_state_j, q)
    # print game
    canvas.delete(ALL)
    nb_cells_ver = len(states)
    for i in range(0, nb_cells_ver):
        nb_cells_hor = len(states[i])
        cell_width = width / nb_cells_hor
        cell_height = height / nb_cells_ver
        for j in range(0, nb_cells_hor):
            canvas.create_rectangle(cell_width * j, cell_height * i, cell_width * (j + 1), cell_height * (i + 1),
                                    fill=get_color(states[i][j]))
            if i == current_state_i and j == current_state_j:
                canvas.create_oval(cell_width * j, cell_height * i, cell_width * (j + 1), cell_height * (i + 1),
                                   fill="red")
    canvas.after(2500, game)


# initialize Q function
initializeQ()
# Launch
width = 300
height = 300
title = "Maze"
window = Tk()
window.title(title)
window.geometry(str(width) + "x" + str(height))
canvas = Canvas(window, width=width, height=height, borderwidth=0, highlightthickness=0)
canvas.pack()
canvas.after(0, game)
window.mainloop()
