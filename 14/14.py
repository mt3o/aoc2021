from collections import Counter, defaultdict

if __name__ == '__main__':
    with open("input.txt") as f:
        # with open("input.txt") as f:
        template = "_"+f.readline().rstrip()+"_"
        f.readline()
        insertions = [_.rstrip() for _ in f.readlines()]

    pairs = ["".join(_) for _ in zip(template, template[1:])]
    workdict = Counter(pairs)

    insertions = {key: value for key, value in (line.split(" -> ") for line in insertions)}

    total_iterations = 40 # part B
    # total_iterations = 10 # part A

    for i in range(total_iterations):

        new_workdict = Counter()

        for adj, insertion in insertions.items():
            if adj in workdict:
                existing_pairs = workdict[adj]
                left = adj[0]
                right = adj[1]
                new_workdict[left + insertion] += existing_pairs
                new_workdict[insertion + right] += existing_pairs

        for pair in workdict.keys():
            if pair not in insertions:
                new_workdict[pair] = workdict[pair]

        print("After", i, "having", sum([_ for _ in new_workdict.values()]))
        workdict = new_workdict
         # NCNBCHB
    accumulator = defaultdict(lambda: 0)
    for pair, value in workdict.items():
        accumulator[pair[0]] += value
    accumulator = sorted(accumulator.items(), key=lambda x: x[1], reverse=True)
    most_common = accumulator[0]
    least_common = accumulator[-2]
    print("Result: ",most_common[1] - least_common[1])
