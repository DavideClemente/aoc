def run():
    file = open('input.txt', 'r')
    content = file.read().splitlines()
    sum = 0
    for p in content:
        l, w, h = map(int, p.split('x'))
        # l = int(l)
        # w = int(w)
        # h = int(h)
        sides = [l, w, h]
        small1 = min(sides)
        sides.remove(small1)
        small2 = min(sides)
        area = (2*l*w + 2*w*h + 2*h*l) + (small1 * small2)
        sum += area
    print(sum)


if __name__ == '__main__':
    run()
