import statistics


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


    incomplete = []
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
                    syntax_errors.append(char)
                    break
        else:
            if len(working_stack):
                incomplete.append([c for c in working_stack])

    completion_scores={
        '(':1,
        '[':2,
        '{':3,
        '<':4
    }
    def get_score(score, incomplete_parts):
        *rest, current = incomplete_parts
        score *= 5
        score += completion_scores[current]
        if rest:
            return get_score(score, rest)
        else:
            return score

    scorings = []
    for incomplete_parts in incomplete:
        scorings.append(get_score(0,incomplete_parts))

    scorings = sorted(scorings)
    middle = statistics.median(scorings)
    print(middle)
