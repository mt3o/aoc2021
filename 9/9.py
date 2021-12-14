if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.readlines()
        #sample:
#         input="""2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678""".split("\n")
        input = [[int(field) for field in line.rstrip()] for line in input]

    row_max = len(input) - 1
    col_max = len(input[0]) - 1

    adjacent_positions = [
        (-1, 0), (0, 1), (0, -1), (1, 0)
    ]

    def get_adjacent_positions(x, y):
        for dx, dy in adjacent_positions:
            ey = y+dy
            ex = x+dx
            if 0 <= ey <=row_max and 0 <= ex <= col_max:
                yield input[ey][ex]



    def validate(field, x, y):
        adj_positions = [p for p in get_adjacent_positions(x, y)]
        r = all(field < a for a in adj_positions)
        return r


    low_spots = [(field,x,y) for y, row in enumerate(input) for x, field in enumerate(row) if validate(field, x, y)]
    risk = sum(field[0]+1 for field in low_spots)
    print(f"{risk=}")
