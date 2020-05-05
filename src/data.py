# Maze Game status
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

# rewards map : in this example
rewards = {
    'R': -1,  # R = Road penalty is agent stays in road (-1 will force agent to move),
    'H': -5,  # H : Hole penalty if agent falls in hole (mud),
    'W': -100,  # W : Water penalty if agent falls in water,
    'G': +100  # G : Goal reward if agent achieves its mission.
}

# possible actions : [name of action : (step_i_axis, step_j_axis)
actions = {
    'UP': (-1, 0),
    'DOWN': (+1, 0),
    'RIGHT': (0, +1),
    'LEFT': (0, -1),
    'STAY': (0, 0)
}

# learning rate
alpha = 0.1

# Eagerness
gamma = 0.9

# initial status
start_position_i = 0
start_position_j = 0

# Tkinter params :
width = 300
height = 300
title = "Maze"
colors = {"W": "#1ae5ef", "H": "#c96134", "R": "#7e9296", "G": "#2ccc44"}
agent_color = "red"
step_wait_time = 750  # in millis
