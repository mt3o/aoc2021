from collections import Counter


def get_int_from_counted_bits(counters):
    bits = [_[0] for _ in counters]
    bits = "".join(bits)
    return int(bits, 2)


def cleanse(data, position, commonity, fallback_value):

    if len(data[0]) <= position:
        raise Exception(f"Index out of range {position=}")

    position_counter = Counter((bit[position] for bit in data))
    counted = position_counter.most_common()
    searched_bit = counted[commonity][0] if counted[0][1] != counted[1][1] else fallback_value

    new_data = [line for line in data if line[position] == str(searched_bit)]

    if not new_data:
        raise Exception("Data reduced to empty list")

    if len(new_data) == 1:
        return new_data[0]
    else:
        return cleanse(new_data, position=position+1, commonity=commonity, fallback_value=fallback_value)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]

        oxygen_bits = cleanse(data, 0, commonity=0, fallback_value=1)
        co2_bits = cleanse(data, 0, commonity=1, fallback_value=0)

        oxygen = int(oxygen_bits,2)
        co2 = int(co2_bits,2)

        r = oxygen * co2
        print(f"{oxygen=} {co2=} {r=}")