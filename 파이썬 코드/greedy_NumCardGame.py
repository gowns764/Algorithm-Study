n, m = map(int, input().split())
min_data = 0

for i in range(n):
    data = list(map(int, input().split()))
    tmp = min(data)
    if i == 0:
        min_data = tmp
    else:
        if min_data < tmp:
            min_data = tmp

print(min_data)