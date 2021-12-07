if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.readlines()

    forward = [int(i) for i in [line.split(" ")[1] for line in input if line.startswith("forward")]]
    down = [int(i) for i in [line.split(" ")[1] for line in input if line.startswith("down")]]
    up = [int(i) for i in [line.split(" ")[1] for line in input if line.startswith("up")]]

    forward = sum(forward)
    down = sum(down)
    up = sum(up)

    result = forward*(down-up)
    print(f"{forward=} {down=} {up=} {result=}")
