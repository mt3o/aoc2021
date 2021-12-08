from collections import namedtuple, defaultdict

vent = namedtuple("Vent", "x1 y1 x2 y2")


def parse_line(line):
    start, end = line.split(" -> ")
    x1, y1 = start.split(",")
    x2, y2 = end.split(",")
    return vent(
        int(x1), int(y1),
        int(x2), int(y2)
    )


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.readlines()

        #         input = """0,9 -> 5,9
        # 8,0 -> 0,8
        # 9,4 -> 3,4
        # 2,2 -> 2,1
        # 7,0 -> 7,4
        # 6,4 -> 2,0
        # 0,9 -> 2,9
        # 3,4 -> 1,4
        # 0,0 -> 8,8
        # 5,5 -> 8,2""".split("\n")

        vents = [parse_line(line) for line in input]
        valid_vents = [v for v in vents if v.x1 == v.x2 or v.y1 == v.y2]
        diagonal_vents = [v for v in vents if v.x1 != v.x2 and v.y1 != v.y2]

        vent_fields_on_map = defaultdict(lambda: 0)

        for vent in valid_vents:
            if vent.x1 == vent.x2:
                start = min(vent.y1, vent.y2)
                end = max(vent.y1, vent.y2)
                for y in range(start, end):
                    key = f'{vent.x1},{y}'
                    vent_fields_on_map[key] += 1
            if vent.y1 == vent.y2:
                start = min(vent.x1, vent.x2)
                end = max(vent.x1, vent.x2)
                for x in range(start, end):
                    key = f'{x},{vent.y1}'
                    vent_fields_on_map[key] += 1

        dangers = [pos for pos, count in vent_fields_on_map.items() if count > 1]
        print(f"{len(dangers)=}")
