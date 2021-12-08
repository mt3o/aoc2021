from math import floor, ceil
from statistics import median, mean

if __name__ == "__main__":
    with open("input.txt") as f:
        input = [int(n) for n in f.readline().split(",")]
    # input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]  # sample

    crab_median = floor(mean(input)) # here instead of median we use mean, it works better :)
    # crab_median = ceil(mean(input)) # note: for other dataset ceil() might work better


    def distance(crab):
        dx = abs(crab - crab_median)
        #now using the school equation for sum of an arithmetic sequence:
        r = (1+dx)*dx/2
        return r

    r = [distance(crab) for crab in input]
    print(sum(r))
                 # 100148861
                 # 100148777
