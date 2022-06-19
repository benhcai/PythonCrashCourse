# Use range with step
nums = list(range(0,11,2))
for num in nums:
    print(num)
print(nums)

# Create list with by editing the range then append
squares = []
for val in range(0, 4):
    square = val**2
    squares.append(square)

print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

# List Comprehensions
doubles = [val*2 for val in range(0,5)]
print(doubles)

# List Slice
players = ['a', 'b', 'c', 'd', 'e', 'f']
print(players[0:2])
slice = players[0:3]
print(slice)
slice[0] = 'z'
print(players)
print(slice)

print(players[1:])
print(players[-3:-1])
