stacks = {
    'A': [],
    'B': [],
    'C': []
}


def print_move(fro, to):
    print('move from ' + str(fro) + ' to ' + str(to))


def print_towers():
    print(''.join(stacks['A']))
    print(''.join(stacks['B']))
    print(''.join(stacks['C']))


def towers(n, fro, to, spare):
    if n == 1:
        print_move(fro, to)
        stacks[to].append(stacks[fro].pop())
        print_towers()
    else:
        towers(n - 1, fro, spare, to)
        towers(1, fro, to, spare)
        towers(n - 1, spare, to, fro)


# Driver code
n = 4
for i in range(n):
    stacks['A'].append(str(i))
print_towers()
towers(n, 'A', 'B', 'C')
# A, C, B are the name of rods
