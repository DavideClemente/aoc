import re
rx = r"\b(?:\w*[aeiyouAEIYOU]){3}\w*"
file = open('input.txt', 'r')
content = file.readlines()
# content = ["jchzalrnumimnmhp"]

print(len([s.strip() for s in content if (re.search(r'([aeiou].*){3,}', s) and
                                          re.search(r'(.)\1', s) and
                                          not re.search(r'ab|cd|pq|xy', s))]))
