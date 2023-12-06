import re
f = open("day3\input.txt", "r")
out = []
lines = ['.' + line.strip() + '.' for line in f.readlines()]
lines.insert(0, '.' * (len(lines[1])))
lines.append('.' * (len(lines[1])))
sum = 0
rows = len(lines)
cols = len(lines[0])
for line in lines:
    print(line)

# 1
# for i, line in enumerate(lines):
#      # a = re.findall(r"(?=\.(\d+)\.)", line)
#     p = re.compile(r"(?=\D(\d+)\D)")
#     power = 1
#     matches = [(match.group(1), match.start(1)-1, match.end(1)) for match in p.finditer(line)]
#     pp = re.compile(r"^\.+$")
#     print(matches)
#     for m in matches:
#         ris = 1
#         print(m)
#         if not pp.match(lines[i-1][m[1]:m[2]+1]):
#             ris = 0
#         if not pp.match(lines[i+1][m[1]:m[2]+1]):
#             ris = 0
        
#         if line[m[1]]!='.' or line[m[2]]!='.':
#             ris=0
#         print(lines[i-1][m[1]:m[2]+1])
#         print(line[m[1]]+" " +m[0]+" "+line[m[2]])
#         print(lines[i+1][m[1]:m[2]+1])
#         if not ris:
#             # print(False)
#             sum+=int(m[0])
#             out.append(m[0])
#         print()
    
print()
# 2
sum  =0 
p = re.compile(r"(\d+)")
p_l = re.compile(r"(\d+)$")
p_r = re.compile(r"^(\d+)")
for i, line in enumerate(lines):
    pow = 1
    stars = [(match.group(0), match.start(0)) for match in re.finditer(r"\*", line)]
    for star in stars:

        s_p = star[1]
        limit_left = s_p - 3 if s_p - 3 > 0 else 0
        limit_right = s_p + 4 if s_p + 4 < len(lines[i])  else len(lines[i])
        print(line[limit_left:s_p] + "*" + line[s_p+1:limit_right])
        print("s_p: " + str(s_p) )
        print(lines[i-1][limit_left:limit_right])
        line_top = lines[i-1]
        nums_top = [n for n in [(match.group(1), match.start(1), match.end(1)) \
                                        for match in p.finditer(line_top) if match.end(1) >= \
                                        s_p and match.start(1) <= s_p+1]]
        print(nums_top)
        nums_top = [n[0] for n in nums_top]
        print([n for n in nums_top])
        line_left = line[limit_left:s_p]
        nums_left = p_l.findall(line_left)
        print(nums_left)
        print( line[limit_left:s_p] + "*" + line[s_p+1:limit_right])
        
        line_right = line[s_p+1:limit_right]
        nums_right = p_r.findall(line_right)
        print(nums_right)
        # print(line[limit_left-1:s_p-1] + " " + str(star) + " " + line[s_p:limit_right])

        print (lines[i+1][limit_left:limit_right])
        line_bottom = lines[i+1]
        nums_bottom = [n[0] for n in [(match.group(1), match.start(1), match.end(1)) \
                                        for match in p.finditer(line_bottom) if match.end(1) >= \
                                        s_p and match.start(1) <= s_p+1]]
        print([n for n in nums_bottom])

        nums = nums_right+nums_bottom+nums_left+nums_top
        print(nums)
        if len(nums) == 2:
            sum+= int(nums[0]) * int(nums[1])
        print()

print(sum)














        # numbers_above = [(match.group(1), match.start(1), match.end(1)) for match in p.finditer(lines[i-1][star[1]-3 if star[1]-3 > 0 else 0:star[1]+5 if star[1]+3<len(lines[i]) else -1])]
        # numbers_below  = [(match.group(1), match.start(1), match.end(1)) for match in p.finditer(lines[i+1][star[1]-2:star[1]])]
        # numbers_left = [(match.group(1), match.start(1), match.end(1)) for match in p.finditer(lines[i][star[1]-3 if star[1]-3 > 0 else 0:star[1]+1])]
        # numbers_right = [(match.group(1), match.start(1), match.end(1)) for match in p.finditer(lines[i][star[1]+1:star[1]+5 if star[1]+3<len(lines[i]) else -1])]
        
        # print(lines[i-1][star[1]-3 if star[1]-3 > 0 else 0:star[1]+5 if star[1]+3<len(lines[i]) else -1])
        # print("NUMS ABOVE: "+str(numbers_above))
        # print(lines[i][star[1]-2:star[1]+1])
        # print("NUMBERS LEFT "+str(numbers_left))
        # print(star)
        # print("NUMBERS RIGHT "+lines[i][star[1]+2:star[1]+5 if star[1]+3<len(lines[i]) else -1])

        # print("NUMBERS RIGHT " + str(numbers_right))
        # print(lines[i+1][star[1]-2 if star[1]-2 > 0 else 0:star[1]+5 if star[1]+3<len(lines[i]) else -1])
        # print("NUMBERS BELOW "+str(numbers_below))
        # print()
        # nums = []
        # nums.append(numbers_above[0][0] if numbers_above else 0) 
        # nums.append(numbers_below[0][0] if numbers_below else 0)
        # nums.append(numbers_left[0][0] if numbers_left else 0)
        # nums.append(numbers_right[0][0] if numbers_right else 0)
        # print(nums)
        # if re.match(lines[i-1][m[1]-3:m[1]+4]) and :


    # pattern = re.compile(r'(?:^|\.)\d+(?:\.|$)')

    # matches = [(match.group(0), match.start()) for match in pattern.finditer(line)]

    # for match, start_index in matches:
    #     print(f"Number: {match}, Index: {start_index}")
    # p = re.compile(r"(?=(?:^|\.)(\d+)(?:\.|$))")
    # print(line)
    # matches = [(match.group(), match.start()) for match in p.finditer(line)] 
    # for match, start_index in matches:
    #     print(f"Number: {match}, Index: {start_index}")
    # index = 0
    # undex = 0
    # nums =[]
    # for char in line:
    #     if char.isdigit():
    #         if index
    #     index+=1
    # print(nums)

    # nums_new = []

    # if nums:
    #     nn = nums[0][0]

    #     for i, num in enumerate(nums):
    #         if i != len(nums) - 1 and num[1] + 1 == nums[i + 1][1]:
    #             nn += nums[i + 1][0]
    #             print("e" + nn)
 

    #         elif i != len(nums) - 1:
    #             nums_new.append((nn, nums.index(num)))
    #             nn = nums[i + 1][0]
    #         #     print("ass" + nn)
    #         # else:
    #         nums_new.append((nn, nums.index(num)))

    #     print(nums_new)

        
# for line in lines:
#     i_nextline = -1
#     i_prevline = -1
#     i = lines.index(line)
#     if i != 0:
#         i_prevline = lines[i-1]
#     if i < len(lines) - 1:
#         i_nextline = lines[i+1]

#     # a = [(m.start(), m.end()) for m in re.finditer(r"(?=\.([0-9]+)\.)", line)]
#     for match in re.finditer(r"(?=\.([0-9]+)\.)", line):
#         s = match.start()
#         e = match.end()
#         print('String match "%s" at %d:%d' % (match.group(), s, e))
#     # print(a)
#     # for t in a:

# for line in lines:
#     print(line) 
# a = ([int(i) for i in re.findall(r"(?=\.([0-9]+)\.)", f.read().replace('\n', ' '))])
# print(a)
# print(str(sum(a)))