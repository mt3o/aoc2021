from collections import Counter


def get_int_from_counted_bits(counters):
    bits = [_[0] for _ in counters]
    bits = "".join(bits)
    return int(bits, 2)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]

        bits_per_line = len(data[0])

        counters = [Counter((bit[bitpos] for bit in data)) for bitpos in range(bits_per_line)]

        most_commons = get_int_from_counted_bits([c.most_common()[0] for c in counters])
        least_commons = get_int_from_counted_bits([c.most_common()[-1] for c in counters])
        r = most_commons * least_commons

        print(f"{most_commons=} {least_commons=} {r=}")