col1 = set(map(int, input().split()))
col2 = set(map(int, input().split()))
print(*sorted(list(filter(lambda x: x % 2 == 0, col1 & col2))))
