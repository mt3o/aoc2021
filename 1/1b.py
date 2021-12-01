if __name__ == "__main__":
    deepness = 0
    deep_window = []
    previous = 9999999
    with open("input.txt", "r") as f:
        deep_window.append(int(f.readline()))
        deep_window.append(int(f.readline()))
        for level in f:
            deep_window.append(int(level))
            if sum(deep_window) > previous:
                deepness += 1
            previous = sum(deep_window)
            deep_window = deep_window[1:3]
    print(deepness)
