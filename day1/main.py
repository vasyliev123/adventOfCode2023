import re
f = open("day1\input.txt", "r")
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
wrds = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0
# 1
# for line in f.readlines():
#     # print([c for c in line if c in nums][0]+" "+[c for c in line[::-1] if c in nums][0])
#     sum += ( int([c for c in line if c in nums][0] + [c for c in line[::-1] if c in nums][0]) )
 
# print(sum)

# 2
for line in f.readlines():
    n = [str(wrds.index(a) +1) if len(a)>1 else str(a) for a in re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))", line)]
    sum += int(n[0]+n[len(n)-1])
    # # nums[wrds.index(c)]
    # first = ""
    # last=""
    # print(line)
    # nums = []
    # if "oneight" in line:
    #     nums += ["8"]
    # if "eightwo" in line:
    #     nums +=["two"]


    # i = [(nums[wrds.index(c)], str(line.index(c))) for c in wrds if line.find(c) != -1]
 
            
    
    # b = [(c, str(line.index(c))) for c in nums if line.find(c) != -1]

    # # print(i)
    # # print(b)
    # c = i + b
    # print(c)
    # # print([m[1] for m in c])
    # min1 = min([int(m[1]) for m in c])
    # # print(min1)
    # first = [s[0] for s in c if int(s[1]) == min1][0]
    
    # max1 = max([int(m[1]) for m in c])
    # last = [s[0] for s in c if int(s[1]) == max1][0]
    # print(first + " " + last)
    # d =  first + last
    # sum += int(d)
 
    # i = [w for w in  [c for c in wrds if line.find(c) != -1]  ]


    # first = ""
    # last = ""
    # n = int([c for c in line if c in nums][0])
    # # print(wrds)
    # print(line)
    # l = line[:n]
    # i =  min([ww for ww in [int(l.find(w)) for w in wrds ] if ww != -1], default="EMPTY")
    # if i == "EMPTY":
    #     first = str(n)
    # else:
    #     first=line.startswith
    # l = line[n:]

    # i1 =  min([ww for ww in [int(l.find(w)) for w in wrds ] if ww != -1], default="EMPTY")

    # # i = min(index for index in [line.find(w) for w in wrds])
    # print(n)
    # print(i)
    # print(i1)
    # if line.index(n) == 0:
    #     first = n
    # if line.index(n) == len(line):
    #     last = n
    
    # print(n)
    # for w in wrds:
    #     if w in line[:n]:
            # print(w)
    # if w:=any(w in line for w in nums):
    #     for w in wrds:
    #         if w in list[:line.find(w)]:
    #             print(nums(wrds.index(w)))

    # # ws = []
    # # new_line = ""
    # # for c in line:
    # #     if c not in nums:
    # #         new_line += c
    # # for w in wrds:
    # #     if w in line:
    # #         ws.append(w)
    
    # # print(ws)
    # print(new_line)

print(sum)