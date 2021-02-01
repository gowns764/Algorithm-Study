from random import randint
import time

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

start_time = time.time()

array.sort()    # 오름차순으로 정렬
first = array[n-1]  # 가장 큰 수
second = array[n-2] # 그 다음 큰 수

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m - count) * second

print(result)

end_time = time.time()
print("시간 :", end_time - start_time)