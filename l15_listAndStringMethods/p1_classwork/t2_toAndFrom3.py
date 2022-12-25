squares = [int(i) ** 2 for i in input().split()]
left, right = [int(i) for i in input().split()]
squares = squares[left:right + 1]
print(sum(squares))
