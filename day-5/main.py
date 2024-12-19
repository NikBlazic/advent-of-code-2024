file = open("day-5/input.txt", "r")
data = file.read()
lines = data.splitlines()

# part 1
updates = []
rules = []
i = 0
sum = 0

while i < len(lines) and lines[i]:
    before, after = lines[i].split('|')
    rules.append((int(before), int(after)))
    i += 1

i += 1

while i < len(lines) and lines[i]:
    update = [int(x) for x in lines[i].split(',')]
    updates.append(update)
    i += 1

def is_valid_order(update, rules):
    
    for before, after in rules:
        
        if before in update and after in update:
            
            if update.index(before) > update.index(after):
                return False
    return True

for update in updates:
    if is_valid_order(update, rules):
        middle_position = len(update) // 2
        sum += update[middle_position]

print("Part 1")
print(f"Sum: {sum}")
print("---"*15)

# part 2
updates = []
rules = []
i = 0
sum = 0

while i < len(lines) and lines[i]:
    before, after = lines[i].split('|')
    rules.append((int(before), int(after)))
    i += 1

i += 1

while i < len(lines) and lines[i]:
    update = [int(x) for x in lines[i].split(',')]
    updates.append(update)
    i += 1

def fix_order(update, rules):
    
    numbers = update.copy()
    changed = True

    while changed:
        changed = False
        for before, after in rules:
            if before in numbers and after in numbers:
                before_idx = numbers.index(before)
                after_idx = numbers.index(after)
                if before_idx > after_idx:
                    numbers[before_idx], numbers[after_idx] = numbers[after_idx], numbers[before_idx]
                    changed = True
    
    return numbers

for update in updates:
    if not is_valid_order(update, rules):
        fixed_update = fix_order(update, rules)
        middle_position = len(fixed_update) // 2
        sum += fixed_update[middle_position]

print("Part 2")
print(f"Sum: {sum}")
print("---"*15)