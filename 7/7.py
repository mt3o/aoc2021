
from statistics import median, mean

if __name__ == "__main__":
    with open("input.txt") as f:
        input = [int(n) for n in f.readline().split(",")]
    # input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]  # sample

    crab_median = round(median(input))
    median_diffs_sum = sum([abs(crab-crab_median) for crab in input])
    print(median_diffs_sum)

    #mean works better than average
    # crab_average = round(mean(input))
    # average_diffs_sum = sum([abs(crab-crab_average) for crab in input])
    # print(average_diffs_sum)
