if __name__ == "__main__":
    name = "input.txt"
    # name = "sample.txt"
    with open(name) as f:
        input = [[c for c in n.rstrip()] for n in f.readlines()]

    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    closings={
        '[':']',
        '(':')',
        '<':'>',
        '{':'}',
    }

    corrupted = []
    incomplete = []
    clear = []

    syntax_errors = []

    for line in input:

        working_stack = []

        for char in line:
            if char in '[{(<':
                working_stack.append(char)
            elif char in ']})>':
                if closings[working_stack[-1]] == char:
                    working_stack.pop()
                else:
                    corrupted.append(line)
                    syntax_errors.append(char)
                    break
        else:
            if len(working_stack):
                incomplete.append(line)
            else:
                clear.append(line)

    total_score = sum([scores[e] for e in syntax_errors])
    print(f"{total_score=}")
