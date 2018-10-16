import sys
import math

number_testcase = int(sys.stdin.readline().rstrip())
inputs = []

t = number_testcase
while t:    
    inputs.append(int(sys.stdin.readline().rstrip()))
    t -= 1

for n in inputs:
    _bit = 0
    _nibble = 0
    _byte = 0
    # if n <= 2:           
    #     _bit = 1
    # elif n > 2 and n <= 8:
    #     _nibble = 1
    # elif n > 8 and n <= 16:
    #     _byte = 1
    if(n % 16 > 0 and n % 16 <= 2):
        _bit = int(math.pow(2, int(n / 16)))
    elif(n % 16 > 2 and n % 16 <= 8):
        _nibble = int(math.pow(2, int(n / 16)))
    elif (n % 16 == 0 or n % 16 > 8):
        _byte = int(math.pow(2, (int(n / 16) - 1)))
        # dividend = int(n / 16)
        # if dividend == 1:
        #     _byte = int(math.pow(2, (int(n / 16) - 1)))
        # else:
        #     _byte = int(math.pow(2, (int(n / 16) - 1)))
    print( _bit, _nibble, _byte)