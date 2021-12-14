from functools import reduce

if __name__ == "__main__":

    # with open("sample.txt") as f:
    with open("input.txt") as f:
        input = [line.rstrip() for line in f.readlines()]

    points = []
    folds = []

    for line in input:
        if "," in line:
            coords = line.split(",")
            points.append((int(coords[0]), int(coords[1])))
        elif "fold along" in line:
            axis, line = line.replace("fold along ", "").split("=")
            folds.append((axis, int(line)))
    def bounce(coord, foldline):
        if coord < foldline:
            return coord
        else:
            return 2 * foldline - coord
        
    def bend(points, axis, line):
        if axis == "y":
            return [(x, bounce(y, line)) for x, y in points]
        if axis == "x":
            return [(bounce(x, line), y) for x, y in points]

    # Sample data:
    # points = bend(points, "y", 7)
    # uniq_points = list(set(points))
    # print("done")

    # Part 1
    # for axis,bendline in [folds[0]]:
    #     points = bend(points, axis, bendline)
    #     points = list(set(points))
    # print("result", len(points))

    for axis,bendline in folds:
        points = bend(points, axis, bendline)
        points = list(set(points))



    max_x = 1+max([p[0] for p in points])
    max_y = 1+max([p[1] for p in points])

    screen = [[" "]*max_x for _ in range(max_y)]
    for x, y in points:
        screen[y][x] = "#"

    for line in screen:
        print("".join(line))
