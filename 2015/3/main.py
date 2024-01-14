def run():
    file = open('input.txt')
    content = file.readline()
    ans = solve(content)
    print(ans)


def solve(path):
    santa = True
    santa_houses = {(0, 0): 1}
    robot_houses = {(0, 0): 1}

    sx, sy = 0, 0
    rx, ry = 0, 0
    for c in path:
        santa = not santa
        if santa:
            if c == '^':
                sy += 1
            elif c == '>':
                sx += 1
            elif c == 'v':
                sy -= 1
            elif c == '<':
                sx -= 1
            if (sx, sy) in santa_houses.keys():
                santa_houses[(sx, sy)] += 1
            else:
                santa_houses[(sx, sy)] = 1
        else:
            if c == '^':
                ry += 1
            elif c == '>':
                rx += 1
            elif c == 'v':
                ry -= 1
            elif c == '<':
                rx -= 1
            if (rx, ry) in robot_houses.keys():
                robot_houses[(rx, ry)] += 1
            else:
                robot_houses[(rx, ry)] = 1

    return len([h for h in santa_houses.values() if h >= 1]) + len([h for h in robot_houses.values() if h >= 1]) - 1


if __name__ == '__main__':
    run()
