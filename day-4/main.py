file = open("day-4/input.txt", "r")
data = file.read()
lines = data.splitlines()

# part 1
count = 0

# left to right
for line in lines:
    for i in range(len(line)):
        if line[i:i+4] == "XMAS":
            count += 1
        if line[i:i+4] == "SAMX":
            count += 1

# all other directions
for y in range(len(lines)):
    line = lines[y]
    for i in range(len(line)):
        if line[i] == "X":
            if y+3 < len(lines) and i+3 < len(line):
                if (lines[y+1][i+1] == "M" and 
                    lines[y+2][i+2] == "A" and 
                    lines[y+3][i+3] == "S"):
                    count += 1
            if y+3 < len(lines) and i-3 >= 0:
                if (lines[y+1][i-1] == "M" and 
                    lines[y+2][i-2] == "A" and 
                    lines[y+3][i-3] == "S"):
                    count += 1
            if y-3 >= 0 and i+3 < len(line):
                if (lines[y-1][i+1] == "M" and 
                    lines[y-2][i+2] == "A" and 
                    lines[y-3][i+3] == "S"):
                    count += 1
            if y-3 >= 0 and i-3 >= 0:
                if (lines[y-1][i-1] == "M" and 
                    lines[y-2][i-2] == "A" and 
                    lines[y-3][i-3] == "S"):
                    count += 1
            if y-3 >= 0:
                if (lines[y-1][i] == "M" and 
                    lines[y-2][i] == "A" and 
                    lines[y-3][i] == "S"):
                    count += 1
            if y+3 < len(lines):
                if (lines[y+1][i] == "M" and 
                    lines[y+2][i] == "A" and 
                    lines[y+3][i] == "S"):
                    count += 1

print("Part 1:")
print(f"Total count: {count}")
print("---"*15)

# part 2
count = 0

for y in range(len(lines)):
    line = lines[y]
    for i in range(len(line)):
        if line[i] == "A":
            if y+1 < len(lines) and y-1 >= 0 and i-1 < len(line) and i+1 < len(line):
                if (lines[y-1][i-1] == "M" and 
                    lines[y-1][i+1] == "M" and
                    lines[y+1][i-1] == "S" and 
                    lines[y+1][i+1] == "S"):
                    count += 1
            if y+1 < len(lines) and y-1 >= 0 and i-1 < len(line) and i+1 < len(line):
                if (lines[y-1][i-1] == "S" and 
                    lines[y-1][i+1] == "S" and
                    lines[y+1][i-1] == "M" and 
                    lines[y+1][i+1] == "M"):
                    count += 1
            if y+1 < len(lines) and y-1 >= 0 and i-1 < len(line) and i+1 < len(line):
                if (lines[y-1][i-1] == "S" and 
                    lines[y-1][i+1] == "M" and
                    lines[y+1][i-1] == "S" and 
                    lines[y+1][i+1] == "M"):
                    count += 1
            if y+1 < len(lines) and y-1 >= 0 and i-1 < len(line) and i+1 < len(line):
                if (lines[y-1][i-1] == "M" and 
                    lines[y-1][i+1] == "S" and
                    lines[y+1][i-1] == "M" and 
                    lines[y+1][i+1] == "S"):
                    count += 1

print("Part 2:")
print(f"Total count: {count}")
print("---"*15)