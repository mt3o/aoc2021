from tqdm import tqdm

# this approach works for days=80 but doesn't for days=256, it takes too long to compute
# this is variation of 6.py

if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.readline()
        input = input.rstrip()
        input = [int(i) for i in input.split(",")]
    # input = [3, 4, 3, 1, 2]  # sample data
    fishes = (input)
    # total_days = 18  # sample data
    total_days = 80 #part1 data
    # total_days = 256 #part2 data
    for _ in tqdm(range(total_days)): #added tqdm to have a progress bar
        fishes = [f-1 for f in fishes]
        breeding = [f for f in fishes if f==-1]
        fishes.extend([8]*len(breeding))
        fishes = [f if f!=-1 else 6 for f in fishes]

    print(len(fishes))
