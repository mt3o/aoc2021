if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.readlines()

#     input ="""forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2""".split("\n")

    depth = 0
    distance = 0
    aim = 0

    for line in input:
        number = int(line.split(" ")[1])
        if line.startswith("forward"):
            distance += number
            depth += number * aim
        if line.startswith("up"):
            aim -= number
            #depth -= number
        if line.startswith("down"):
            aim += number
            #depth += number

    result = distance * (depth)
    print(f"{depth=} {aim=} {result=}")
