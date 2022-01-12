import pygame, sys, os, random, math
a = 0
d = 0

def dice(type, amount):
    results = []
    total = 0
    for i in range(amount):
        number = random.randint(1, type)
        results.append(number)
        total += number
    return results, total

def check(a, d, attack, defence):
    attack.sort(reverse=True)
    defence.sort(reverse=True)
    for i in range(2):
        if defence[i] >= attack[i]:
            d += 1
        else:
            a += 1
    return a, d

def roll_risk(a, d): # Two ways to return specifiec values from a function.
    attack = dice(6, 3)[0] # End the function with [num] to get a specific value.
    defence, *_ = dice(6, 2) # Ask for *_ to return all values except specifically defined ones to _.
    a, d = check(a, d, attack, defence)
    return a, d

for i in range(1000000): # This takes 10-20 seconds for 1,000,000 tests
    a, d = roll_risk(a, d)

print('Attack:', a)
print('Defence:', d)