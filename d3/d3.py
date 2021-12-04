import numpy as np
from statistics import mode
from collections import Counter

def char_to_str(c_list: list):
    r = ""
    for c in c_list:
        r += c
    return r

f = open("d3/input.txt", "r")
lines = f.readlines()
f.close()

parsed = [list(l.strip()) for l in lines]

# print(parsed)

m = np.array(parsed)

# get column size
col_size = m.shape[1]

result = []

for i in range(col_size):
    most_common = mode(m[:,i])
    result.append(most_common)

a_str  = char_to_str(result)
a = int(a_str, base=2)

sum = 0b111111111111
b = sum - a
print(result)
print(bin(a))
print(bin(b))
print("Power consumption of submarine is:",a*b)


# Part 2
def get_most(l: list):
    counter = Counter(l)
    if counter['1'] >= counter['0']:
        return '1'
    return '0'
def get_least(l: list):
    counter = Counter(l)
    if counter['1'] < counter['0']:
        return '1'
    return '0'

most = []
least = []
most_rows = m
least_rows = m
a = None
b = None
for i in range(col_size):
    # process column i
    if a is None:
        most_common = get_most(most_rows[:,i])
        most.append(most_common)
        # filter rows by most and least
        most_filter = np.asarray(most_common)
        most_rows = most_rows[np.in1d(most_rows[:, i], most_filter)]
        # short circurt the loop when only one row left
        if len(most_rows) == 1:
            a = most_rows[0]

    if b is None:
        least_common = get_least(least_rows[:,i])
        least.append(least_common)
        least_filter = np.asarray(least_common)
        least_rows = least_rows[np.in1d(least_rows[:, i], least_filter)]
        if len(least_rows) == 1:
            b = least_rows[0]

a = int(char_to_str(a), base=2)
b = int(char_to_str(b), base=2)
print(a, b)
print("life support level is:", a*b)
    
