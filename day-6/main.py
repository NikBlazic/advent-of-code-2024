file = open("day-6/input.txt", "r")
data = file.read()
lines = data.splitlines()

# Part 1
direction = "up"
guard = None

directions = {
    "up": (0, -1),
    "right": (1, 0),
    "down": (0, 1),
    "left": (-1, 0)
}

turn_right = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up"
}

for row in range(len(lines)):
    for space in range(len(lines[row])):
        if lines[row][space] == "^":
            guard = (space, row)
            break

visited = [guard]

while True:
    dx, dy = directions[direction]
    next_x = guard[0] + dx
    next_y = guard[1] + dy
    
    if (next_x < 0 or next_x >= len(lines[0]) or 
        next_y < 0 or next_y >= len(lines)):
        break
        
    if lines[next_y][next_x] == "#":
        direction = turn_right[direction]
    else:
        guard = (next_x, next_y)
        
    if guard not in visited:
        visited.append(guard)

print("Part 1:")
print(f"Distinct positions visited: {len(visited)}")
print("---"*15)

# Part 2