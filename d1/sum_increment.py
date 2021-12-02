f = open("./input.txt", "r")
lines = f.readlines()
f.close()

nums = [int(l.strip()) for l in lines]

inc_count = 0
length = len(nums)

for i in range(length - 3):
    print(i, nums[i])
    print(i + 3, nums[i + 3])
    head = nums[i]
    tail = nums[i + 3]
    if tail > head:
        inc_count += 1

print(inc_count)
