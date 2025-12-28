import time
outer = 10_000
inner = 10_000
sumv = 0
t1 = time.perf_counter()
for _ in range(outer):
    for _ in range(inner):
        sumv += 1
t2 = time.perf_counter()
print({"lang":"python", "time": t2 - t1, "sum": sumv})
