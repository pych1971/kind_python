set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
s = set_a ^ set_b
print(*sorted(s))
