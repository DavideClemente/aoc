import re
file = open('input.txt', 'r')
content = file.readlines()

print(len([
    s.strip() for s in content
    if re.search(r'(.{2}).*?\1', s)
    and re.search(r'(.).\1', s)
]))
