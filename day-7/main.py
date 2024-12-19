file = open("day-7/input.txt", "r")
data = file.read()
lines = data.splitlines()

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        else:
            result *= numbers[i + 1]
    return result

def can_make_target(numbers, target_sum):
    n_operators = len(numbers) - 1
    
    for i in range(2 ** n_operators):
        operators = []
        for j in range(n_operators):
            if (i >> j) & 1:
                operators.append('+')
            else:
                operators.append('*')
        
        result = evaluate_expression(numbers, operators)
        if result == target_sum:
            return True
    
    return False

cases = 0

for line in lines:
    target_sum, numbers = line.split(":")
    target_sum = int(target_sum)
    numbers = numbers.split()
    numbers = [int(x) for x in numbers]

    if can_make_target(numbers, target_sum):
        cases += target_sum

print(cases)