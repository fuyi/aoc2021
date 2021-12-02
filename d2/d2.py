from functools import reduce


f = open("./input.txt", "r")
lines = f.readlines()
f.close()

lines = [tuple(l.strip().split(" ")) for l in lines]


##
# simple loop solution
##
x , y = 0, 0

for (i, num) in lines:
    num = int(num)
    # print(i, num)
    if i == 'forward':
        x += num
    elif i == 'up':
        y -= num
    elif i == 'down':
        y +=num

print(x*y)


aim, h, d = 0,0,0

for (i, num) in lines:
    num = int(num)
    # print(i, num)
    if i == 'forward':
        h += num
        d += num* aim
    elif i == 'up':
        aim -= num
    elif i == 'down':
        aim +=num

print(h*d)

##
# functional solution
##
def coordinate(a, b):
    # print(a, b)
    num = int(b[1])
    if b[0] == 'forward':
        return (a[0]+num, a[1])
    elif b[0] == 'up':
        return (a[0], a[1] - num)
    elif b[0] == 'down':
        return (a[0], a[1] + num)

result  = reduce(coordinate, lines, (0,0))

print(reduce(lambda a, b: a*b, result, 1))

def with_aim(a, b):
    num = int(b[1])
    if b[0] == 'forward':
        return (a[0], a[1]+num, a[2]+ num*a[0])
    elif b[0] == 'up':
        return (a[0] - num, a[1], a[2])
    elif b[0] == 'down':
        return (a[0] + num, a[1], a[2])

result_with_aim = reduce(with_aim, lines, (0,0,0))
# print(result_with_aim)
print(result_with_aim[1]* result_with_aim[2])