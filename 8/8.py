D0 = set("abcefg")
D1 = set("be")
D2 = set("acdeg")
D3 = set("acdfg")
D4 = set("bcdf")
D5 = set("abdfg")
D6 = set("abdefg")
D7 = set("acf")
D8 = set("abcdefg")
D9 = set("abcdfg")


class Note:
    signals = []
    digits = []

    def __init__(self, line):
        signals, digits = line.replace("\n", "").split("|")

        self.signals = [set(digit) for digit in signals.split(" ") if digit != ""]
        self.digits = [set(digit) for digit in digits.split(" ") if digit != ""]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.readlines()
        data = [Note(line) for line in input]

        easy_lens = [len(d) for d in [D7, D1, D4, D8]]

        count = 0
        for n in data:
            for digit in n.digits:
                if len(digit) in easy_lens:
                    count += 1
        print(f"part1 {count=}")

        part2_sum = 0

        mapping = {}
        for n in data:
            mapping['1'] = [s for s in n.signals if len(s) == len(D1)][0]
            mapping['4'] = [s for s in n.signals if len(s) == len(D4)][0]
            mapping['7'] = [s for s in n.signals if len(s) == len(D7)][0]
            mapping['8'] = [s for s in n.signals if len(s) == len(D8)][0]

            for d in n.signals:
                # with len 6 we have: 6 9 0 they differ by 1 segment
                if len(d) == 6:
                    if len(mapping['1'] - d) == 1:
                        mapping['6'] = d
                    elif len(mapping['4'] - d) == 0:
                        mapping['9'] = d
                    elif len(mapping['4'] - d) == 1:
                        mapping['0'] = d
            # now we have  0 1 4 6 7 8 9, must find 2 3 5
            top_right = (mapping['1'] - mapping['6']).pop()

            for d in n.signals:
                if len(d) == 5:
                    if len(mapping['1'] - d) == 0:  # 1 and 5 have only top right segment common, so subtracting gives 0
                        mapping['3'] = d
                    elif top_right in d:
                        mapping['2'] = d
                    else:
                        mapping['5'] = d

            rmapping = {frozenset(v): k for k, v in mapping.items()}

            d1 = rmapping[frozenset(n.digits[0])]
            d2 = rmapping[frozenset(n.digits[1])]
            d3 = rmapping[frozenset(n.digits[2])]
            d4 = rmapping[frozenset(n.digits[3])]

            part2_sum += int(f"{d1}{d2}{d3}{d4}")
        print(f"{part2_sum=}")
"""
0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""
