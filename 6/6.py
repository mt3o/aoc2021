from collections import deque

from tqdm import tqdm

# this approach works for days=80 but doesn't for days=256, it takes too long to compute

if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.readline()
        input = input.rstrip()
        input = [int(i) for i in input.split(",")]
    # input = [3, 4, 3, 1, 2]  # sample data
    fishes = deque(input)
    # total_days = 18  # sample data
    total_days = 80 #part1 data
    # total_days = 256 #part2 data
    for _ in tqdm(range(total_days)): #added tqdm to have a progress bar
        for i in range(len(fishes)):
            fishes[0] -= 1
            if fishes[0] == -1:
                fishes[0] = 6
                fishes.append(8)
            fishes.rotate(-1)  # rotate to left, passing 0 el to the end
    print(len(fishes))
