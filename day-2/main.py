file = open("day-2/input.txt", "r")
data = file.read()
lines = data.splitlines()

safe_count = 0

# part 1
for line in lines:
    nums = [int(x) for x in line.split()]
    is_safe = True
    
    is_increasing = nums[1] > nums[0]
    
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        
        if abs(diff) < 1 or abs(diff) > 3:
            is_safe = False
            break
            
        if is_increasing and diff <= 0:
            is_safe = False
            break
            
        if not is_increasing and diff >= 0:
            is_safe = False
            break
    
    if is_safe:
        safe_count += 1

# part 2
def is_sequence_safe(nums):
    if len(nums) < 2:
        return True
        
    is_increasing = nums[1] > nums[0]
    
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        
        if abs(diff) < 1 or abs(diff) > 3:
            return False
            
        if is_increasing and diff <= 0:
            return False
            
        if not is_increasing and diff >= 0:
            return False
    
    return True

safe_count = 0

for line in lines:
    nums = [int(x) for x in line.split()]
    
    if is_sequence_safe(nums):
        safe_count += 1
        continue
        
    for i in range(len(nums)):
        test_nums = nums[:i] + nums[i+1:]
        if is_sequence_safe(test_nums):
            safe_count += 1
            break

print("safe:", safe_count)
print("not safe:", len(lines) - safe_count)