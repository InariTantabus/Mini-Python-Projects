import sys, os, random

# characters = a-z A-Z 0-9
characters = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def gen_password(chars, length, type):
    if type == 'str':
        password = ''
    else:
        password = []
    for i in range(0, length):
        password += (chars[random.randint(1, len(chars) - 1)])
    return password

def numberToBase(num, base): # I did not write this
    if num == 0:
        return [0]
    digits = []
    while num:
        digits.append(int(num % base))
        num //= base
    return digits[::-1] # [::-1] reverses the order of the list

def crack(chars, num):
    base = len(chars)
    check = numberToBase(num, base)
    for i in range(0, len(check)):
        check[i] = chars[check[i]]
    return check

cracked_password = []
pass_num = 0

shown_password = ''
shown_crack = ''

stored_pasword = gen_password(characters, 4, 'list')
print(stored_pasword)
for i in range(0, len(stored_pasword)):
    shown_password += stored_pasword[i]
print(shown_password)

running = True
while running:
    if cracked_password == stored_pasword:
        for i in range(0, len(cracked_password)):
            shown_crack += cracked_password[i]
        print(shown_crack)
        print(pass_num)
        running = False
    else:
        cracked_password = crack(characters, pass_num)
        pass_num += 1