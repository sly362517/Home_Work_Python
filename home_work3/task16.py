input()
lst = map(int, (input().split()))
n = int(input())
inc = 0
for i in lst:
    if i == n:
        inc += 1
print(inc)