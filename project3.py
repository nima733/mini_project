import random
from time import time

OPERATOR = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATOR)

    expr = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input('Press any key to start!!')
print('--------------------------')
start_time = time()
for i in range(TOTAL_PROBLEMS):
    expr1, answer1 = generate_problem()
    while True:
        guess = input("Problem #: " + str(i + 1) + ' ' + expr1 + ' = ')
        if guess == str(answer1):
            break
        wrong += 1
end_time = time()
total_time = round(end_time - start_time, 2)
print('-------------------')
print(f'Nice work you finished in {total_time} second')
