import sys

number_testcase = int(sys.stdin.readline().rstrip())
inputs = []

t = number_testcase
while t:    
    inputs.append(sys.stdin.readline().rstrip().split(' '))
    t -= 1

def get_turn(chef_point, cook_point, serve_point):
    total_score = chef_point + cook_point
    if total_score % serve_point == 0:
        if int(total_score / serve_point) % 2 == 0:
            return "CHEF"
        else:
            return "COOK"
    else:
        if (int(total_score / serve_point) + 1) % 2 == 0:
            return "COOK"
        else:
            return "CHEF"


for item in inputs:
    print(get_turn(int(item[0]), int(item[1]), int(item[2])))