#!/usr/bin/env python3
# Authur ID: cjack4

def add(number1, number2):
    try:
        return int(number1) + int(number2)
    except:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        return lines
    except:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                 # 15
    print(add('10', 5))              # 15
    print(add('abc', 5))             # error: could not add numbers
    print(read_file('seneca2.txt'))  # ['Line 1\n', 'Line 2\n', 'Line 3\n']
    print(read_file('file10000.txt'))# error: could not read file
