import sys, os, random, math

def dice(sides=6, amnt=1):
    results = []
    for i in range(amnt):
        results.append(random.randint(1, sides))
    
    return results

counter6 = 0
amnt = 100000
for i in range(amnt):
    results = dice(amnt=6)
    if 6 in results:
        counter6 += 1

counter12 = 0
for i in range(amnt):
    results = dice(amnt=12)
    if 6 in results:
        results = sorted(results)
        results.pop()
        if 6 in results:
            counter12 += 1

counter18 = 0
for i in range(amnt):
    results = dice(amnt=18)
    if 6 in results:
        results = sorted(results)
        results.pop()
        if 6 in results:
            results.pop()
            if 6 in results:
                counter18 += 1

print(counter6)
print(counter12)
print(counter18)