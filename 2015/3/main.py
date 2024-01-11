def run():
    file = open('input.txt')
    content = file.readline()
    ans = solve(content)
    print(ans)


def solve(path):
    houses = {(0, 0): 1}
    x, y = 0, 0
    for c in path:
        if c == '^':
            y += 1
        elif c == '>':
            x += 1
        elif c == 'v':
            y -= 1
        elif c == '<':
            x -= 1
        if (x, y) in houses.keys():
            houses[(x, y)] += 1
        else:
            houses[(x, y)] = 1
    return len([h for h in houses.values() if h >= 1])


if __name__ == '__main__':
    run()
