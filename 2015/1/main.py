def run():
    file = open('input.txt', 'r')
    content = file.read()
    balance = 0
    for i, c in enumerate(content):
        if c == '(':
            balance += 1
        if c == ')':
            balance -= 1
        if balance == -1:
            break
    print(i)


if __name__ == '__main__':
    run()
