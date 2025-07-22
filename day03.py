import re

mul_pattern = r'mul\((\d+),(\d+)\)'
do_pattern = r'do\(\)'
dont_pattern = r"don't\(\)"

def evaluate(s: str) -> int:
    # Match any of: do(), don't(), mul(x,y)
    token_pattern = r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)"
    tokens = re.finditer(token_pattern, s)

    enabled = True
    total = 0

    for match in tokens:
        token = match.group(0)
        if token == 'do()':
            enabled = True
        elif token == "don't()":
            enabled = False
        else:
            if enabled:
                x = int(match.group(1))
                y = int(match.group(2))
                total += x * y
    return total

with open("input03.txt") as f:
    lines = f.read()
    result = evaluate(lines)

print(result)
