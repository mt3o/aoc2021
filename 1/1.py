
if __name__ == "__main__":
    previous = 99999
    deepness = 0
    with open("input.txt", "r") as f:
        for levelS in f.readlines():
            level = int(levelS)
            if level > previous:
                deepness += 1
            previous = level
    print(deepness)
