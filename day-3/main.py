file = open("day-3/input.txt", "r")
data = file.read()
lines = data.splitlines()


total_sum = 0

# part 1
for line in lines:
    i = 0
    while i < len(line):
        if line[i:i+4] == "mul(":
            i += 4
            num1 = ""
            while i < len(line) and (line[i].isdigit()):
                num1 += line[i]
                i += 1
            
            if i < len(line) and line[i] == ",":
                i += 1
                num2 = ""
                while i < len(line) and (line[i].isdigit()):
                    num2 += line[i]
                    i += 1
                
                if i < len(line) and line[i] == ")":
                    if num1 and num2:
                        result = int(num1) * int(num2)
                        total_sum += result
        i += 1

print("Part 1:")
print(f"Total sum: {total_sum}")
print("---"*15)

# part 2
enabled = True
total_sum = 0

for line in lines:
    i = 0
    while i < len(line):

        if line[i:i+7] == "don't()":
            enabled = False

        if line[i:i+4] == "do()":
            enabled = True

        if enabled == False:
            i += 1
            continue

        if line[i:i+4] == "mul(":
            i += 4
            num1 = ""
            while i < len(line) and (line[i].isdigit()):
                num1 += line[i]
                i += 1
            
            if i < len(line) and line[i] == ",":
                i += 1
                num2 = ""
                while i < len(line) and (line[i].isdigit()):
                    num2 += line[i]
                    i += 1
                
                if i < len(line) and line[i] == ")":
                    if num1 and num2:
                        result = int(num1) * int(num2)
                        total_sum += result
        i += 1
        
print("Part 2:")
print(f"Total sum: {total_sum}")
print("---"*15)