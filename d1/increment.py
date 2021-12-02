f = open("./input.txt", "r")
lines = f.readlines()
f.close()

nums = [int(l.strip()) for l in lines]

inc_count = 0
length = len(nums)

for i in range(length - 1):
    if nums[i + 1] > nums[i]:
        inc_count += 1


print(inc_count)
