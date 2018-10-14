import sys

number_testcase = int(sys.stdin.readline().rstrip())
inputs = []

t = number_testcase
while t:    
    inputs.append(int(sys.stdin.readline().rstrip()))
    t -= 1

def get_population(N):
    time = N
    bit = 0
    nibble = 0
    byte = 0
    while time:

        time -= 1

for item in inputs:
    print(get_population(item))