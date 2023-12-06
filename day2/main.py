import re
f = open("day2\input.txt", "r")
sum = 0
rules = {
    "blue": 14,
    "red": 12,
    "green": 13
}
#2
for line in f.readlines():
    n = re.findall(r"([0-9]+)\s(blue|red|green)", line)
    sum+=max([int(s[0]) for s in n if s[1]=="blue"])*max([int(s[0]) for s in n if s[1]=="red"])*max([int(s[0]) for s in n if s[1]=="green"])

# 1
# for line in f.readlines():
#     if 1 not in [1 if int(i[0]) > rules[i[1]] else 0 for i in re.findall(r"([0-9]+)\s(blue|red|green)", line.split(':')[1])]:
#         sum+=int(re.findall(r"([0-9]+)", line.split(':')[0])[0])

# print(sum)
    # [a for a in [s[0] for s in n if]]
    # print(n)
print(sum)