with open('d4/input.txt', 'r') as file:
    data = file.read()

data = data.split('\n\n')
data = [item.replace('\n', ' ') for item in data]
# get playing numbers and boards
nums, boards = data[0], data[1:]
# preprocessing numbers and boards, store in list
nums = list(map(lambda x: int(x), nums.split(',')))
boards = [[int(i) for i in b.split()] for b in boards]
print(nums)
print(len(boards))


# list all possible winning combinations
WINS = [
    {0,1,2,3,4},
    {5,6,7,8,9},
    {10,11,12,13,14},
    {15,16,17,18,19},
    {20,21,22,23,24},
    {0,5,10,15,20},
    {1,6,11,16,21},
    {2,7,12,17,22},
    {3,8,13,18,23},
    {4,9,14,19,24},
]

def winning_check(marked: set, wins: list[set]) -> bool:
    """Given the marked index in boards, 
    check if it is super set of winning combs or not
    """
    for win in wins:
        if win.issubset(marked):
            return (True, win)
    return (False, None)

# unit test the winning_check function
test_a = {10,11,12,13,14}
assert(winning_check(test_a, WINS)[0])
test_b = {10,11,12,13,14,15}
assert(winning_check(test_b, WINS)[0])
test_c = {10,11,13,14,15}
assert(not winning_check(test_c, WINS)[0])

# mark the boards
# initialize the mark array
marks = [[] for b in boards]
# keep board wins in a array
win_order = []


# Part 1:
for num in nums:
    for i, b in enumerate(boards):
        # skip board which wins already
        if i in win_order:
            continue
        # check number index in the board, add to mark
        try:
            ind = b.index(num)
            marks[i].append(ind)
        except ValueError:
            continue
        # board wins the game
        is_win, which_win = winning_check(marks[i], WINS)
        if is_win:
            # get all marked values
            marked_values = [b[index] for index in marks[i]]
            unmarked = set(b) - set(marked_values)
            # put board index into win_order array
            win_order.append(i)
            
            print("all unmarked values are:", unmarked)
            print(f"board {i} wins the game with marked index {marks[i]}")
            print(f"winning set {which_win}, when the number hits {num}")
            print("part one result is:", sum(unmarked) * num)

# Part 2:
print("The win order is:", win_order)
