from collections import deque, Counter, defaultdict

from tqdm import tqdm

if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.readline()
        input = input.rstrip()
        input = [int(i) for i in input.split(",")]
    # input = [3, 4, 3, 1, 2]  # sample data
    fishes = (input)
    # total_days = 18  # sample data
    # total_days = 80 #part1 data
    total_days = 256  # part2 data
    fish_tank = deque([0]*9)

    for f in Counter(fishes).items():
        age, count = f
        fish_tank[age]=count

    for _ in tqdm(range(total_days)):  # added tqdm to have a progress bar
        breed = fish_tank.popleft()
        fish_tank[6] += breed  #adult fishes go back to the pool, resetting counter to 6
        fish_tank.append(breed)  #newbord fishes have counter=10, they are at end of the pool

    print(sum(fish_tank)) # indices=age, value=count, we can just sum the counts
