import numpy as np

matrix = np.zeros((1000, 1000))

with open('input.txt', 'r') as file:
    content = list(map(str.strip, file.readlines()))
# content = ["toggle 0,0 through 999,999"]


def turn(on_of, x1, y1, x2, y2):
    if on_of:
        matrix[y1:y2+1, x1:x2+1] += 1
    else:
        matrix[y1:y2+1, x1:x2 +
               1] = np.clip(matrix[y1:y2+1, x1:x2+1] - 1, 0, None)


def toggle(x1, y1, x2, y2):
    matrix[y1:y2+1, x1:x2+1] += 2


for line in content:
    cmd = line.split(' ')
    if cmd[0] == 'turn':
        [x1, y1] = map(int, cmd[2].split(','))
        [x2, y2] = map(int, cmd[4].split(','))
        turn(True if cmd[1] == 'on' else False, x1, y1, x2, y2)
    elif cmd[0] == 'toggle':
        [x1, y1] = map(int, cmd[1].split(','))
        [x2, y2] = map(int, cmd[3].split(','))
        toggle(x1, y1, x2, y2)

# print(np.count_nonzero(matrix == 1))
print(int(matrix.sum()))
