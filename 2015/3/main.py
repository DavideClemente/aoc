def run():
    file = open('input.txt')
    content = file.readline()
    ans = solve(content)
    print(ans)


def solve(path):
    santa = True
    houses = [(0, 0)]

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
            houses.append((sx, sy))
        else:
            if c == '^':
                ry += 1
            elif c == '>':
                rx += 1
            elif c == 'v':
                ry -= 1
            elif c == '<':
                rx -= 1
            houses.append((rx, ry))

    return len(set(houses))


if __name__ == '__main__':
    run()
