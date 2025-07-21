safe_reports = 1000 # since we know number of lines, otherwise count number of lines
bad_reports = [] # array for storing the bad reports

def report_check(nums: list[int]) -> bool:
    diffs_array = [] # initialize array for storing differences

    # Iterate through levels and calculate differences
    for i in range(len(nums) - 1):
        diffs = int(nums[i + 1]) - int(nums[i])
        # Add to difference array
        diffs_array.append(diffs)

    # Check if levels are increasing or decreasing
    is_incr = all(ele > 0 for ele in diffs_array)
    is_decr = all(ele < 0 for ele in diffs_array)

    # If increasing, check if difference is 1-3 inclusive
    if is_incr and not is_decr:
        return all(1 <= el <= 3 for el in diffs_array)

    # If decreasing, check if difference -3 to -1 inclusive
    elif not is_incr and is_decr:
        return all(-3 <= el <= -1 for el in diffs_array)

    # If no change
    else:
        return False

with open("input02.txt", 'r') as f:
    lines = f.readlines() # read all lines

### PART 1: Generate safety report without dampener
for line in lines:
    # Remove whitespace and make string arrays for each line
    line = line.strip().split()

    # Initialize array for storing levels
    levels = []

    # Iterate through each line and make them integer arrays
    for element in range(len(line)):
        levels.append(int(line[element]))

    # Generate diffs and check for conditions
    if not report_check(levels):
        # Decrement safe report counter and add to bad report array
        bad_reports.append(line)
        safe_reports -= 1

print(safe_reports) # score for part 1

### PART 2: Generate safety report with dampener
# Iterate through each number in each report
for report in bad_reports:
    for j in range(len(report)):
        # Slice array to remove jth element
        trial = report[:j] + report[j + 1:]
        # Check for conditions and break loop if safe report found
        if report_check(trial):
            safe_reports += 1
            break

print(safe_reports) # score for part 2

# chatgpt generated
# safe_reports = 1000
# with open("input02.txt", 'r') as f:
#     lines = f.readlines()
#
# for line in lines:
#     line = list(map(int, line.strip().split()))
#     diffs = [line[i+1] - line[i] for i in range(len(line) - 1)]
#
#     # Check if strictly increasing or strictly decreasing
#     is_increasing = all(d > 0 for d in diffs)
#     is_decreasing = all(d < 0 for d in diffs)
#
#     if is_increasing or is_decreasing:
#         # Now check that each difference is between 1 and 3
#         if all(1 <= abs(d) <= 3 for d in diffs):
#             continue  # This is a valid report
#     # Otherwise, decrement safe_reports
#     safe_reports -= 1
#
# print(safe_reports)
# safe_reports = 1000
# with open("input02.txt", 'r') as f:
#     lines = f.readlines()
# for line in lines:
#     nums = list(map(int, line.strip().split()))
#
#     if not report_check(nums):
#         safe_reports -= 1
#         bad_reports.append(nums)
#
# print("Bad Reports:", bad_reports)
# print(safe_reports)
