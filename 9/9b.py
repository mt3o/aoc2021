from collections import namedtuple

if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.readlines()
        #sample:
#         input="""
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678""".lstrip().split("\n")
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
                yield ey, ex

    def get_adjacent_values(x, y):
        for ey, ex in get_adjacent_positions(x,y):
            yield input[ey][ex]



    def validate(field, x, y):
        adj_positions = [p for p in get_adjacent_values(x, y)]
        return all(field < a for a in adj_positions)



    low_spots = [(field,y,x) for y, row in enumerate(input) for x, field in enumerate(row) if validate(field, x, y)]

    basin = namedtuple("Basin", "level x y fields")
    basins = [basin(spot[0], spot[1],spot[2],[(spot[1],spot[2], spot[0])]) for spot in low_spots]

    grown=True
    while grown:
        grown = False

        for b in basins:
            for field_y, field_x, current_height in b.fields:

                for adj_y, adj_x in get_adjacent_positions(field_x, field_y):
                    tested_height = input[adj_y][adj_x]
                    #if field is already assigned, skip
                    if (adj_y, adj_x, tested_height) in (field for basin in basins for field in basin.fields):
                        continue
                    if input[adj_y][adj_x] != 9 and input[adj_y][adj_x] > current_height:
                        b.fields.append((adj_y, adj_x,tested_height))
                        grown = True

    bazin_sizes = [len(basin.fields) for basin in basins]
    bazin_sizes = sorted(bazin_sizes, reverse=True)
    largest_three = bazin_sizes[0]*bazin_sizes[1]*bazin_sizes[2]
    print(f"{largest_three=}")


