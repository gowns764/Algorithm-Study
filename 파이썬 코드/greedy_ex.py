from random import randint
import time

start_time = time.time()

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)

end_time = time.time()
print("시간 :", end_time - start_time)