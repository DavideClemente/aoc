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
        ribbon = 2*small1 + 2*small2
        bow = l*w*h
        area = ribbon + bow
        sum += area
    print(sum)


if __name__ == '__main__':
    run()
