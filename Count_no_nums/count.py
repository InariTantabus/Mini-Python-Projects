import sys, os

def count_no_nums():
    ten = len('..........')
    hundred = ten*ten
    for i in range(hundred):
        print(int(i+ten/ten))

count_no_nums()