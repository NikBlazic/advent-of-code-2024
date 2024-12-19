file = open("day-1/input.txt", "r")
data = file.read()
lines = data.splitlines()

right = []
left = []

for line in lines:
    numbers = line.split()
    right.append(int(numbers[0]))
    left.append(int(numbers[1]))

# part 1
right.sort()
left.sort()

total_distance = 0
for i in range(len(right)):
    distance = abs(right[i] - left[i])
    total_distance += distance

print(f"Total distance: {total_distance}")

count = 0
sum = 0

# part 2
for number in left:
    for search in right:
        if number == search:
            count += 1
    sum += number * count
    count = 0

print(sum)