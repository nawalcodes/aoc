import re
left = [] # left array
right = [] # right array
dist_sum = 0
with open("input01.txt", 'r') as f:
    for line in f:
        # removes all whitespace
        line = re.sub(r"\s+", "", line, flags=re.UNICODE)

        # since we know the numbers are made up of 5 digits, can split accordingly
        int1 = int(line[0:5])
        int2 = int(line[5:10])

        # append to individual arrays
        left.append(int1)
        right.append(int2)

    # once all numbers are added, sort arrays
    left.sort()
    right.sort()

    ## part 1: find total distance

    # for each element in the left array
    for element in range(len(left)):
        # calculate absolute distance between respective elements of both arrays
        dist_sum += abs(left[element] - right[element])
    print(dist_sum)

    ## part 2: similarity score
    score = 0

    # iterate through each element in left array
    for i in range(len(left)):

        # for a single element in left array, iterate through each element in right array
        for j in range(len(right)):
            count = 0

            # increment counter after finding a match
            if left[i] == right[j]:
                count += 1

            # multiply counter with left element and increment score
            score += left[i] * count

            # increment inner iterator
            j += 1

        # increment outer iterator
        i += 1

    print(score)

#from collections import Counter

# Read and parse input
# with open("input01.txt") as f:
#     lines = f.readlines()
#
# left = []
# right = []
#
# for line in lines:
#     print(line.strip().split())
#     a, b = map(int, line.strip().split())
#     left.append(a)
#     right.append(b)
#
# left_sorted = sorted(left)
# right_sorted = sorted(right)
#
# part1 = sum(abs(a - b) for a, b in zip(left_sorted, right_sorted))
# print("Part 1:", part1)


