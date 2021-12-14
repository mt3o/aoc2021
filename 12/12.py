from collections import deque
from typing import List, Tuple

# input = "sample1.txt"
input = "input.txt"


def find_all_paths(success, graph, current_path, filter):
    # always start, well, in the start point
    # and we have only 1 candidate for the start. The starting point.

    # then we will try to extend it with possible paths, giving back to the active list.
    # if we hit end, we can remove that path from the list, and mark as success
    # if we hit dead end, well, we dont explore it anymore

    current_node = current_path[-1]

    if current_node == "end":
        success.append(current_path)
        return True

    possible_vertices = [
        target for source, target
        in graph
        if source == current_node and filter(target, current_path)
    ]
    for candidate in possible_vertices:
        find_all_paths(success, graph, [*current_path, candidate], filter)


def cleanup(paths):
    """Remove non unique paths"""
    stringified_paths = [" ".join(s) for s in paths]
    uniqueue_paths = set(stringified_paths)
    paths = [p.split(" ") for p in uniqueue_paths]
    return paths


if __name__ == "__main__":
    with open(input) as f:
        input_graph: List[List[str]] = [line.rstrip().split("-") for line in f.readlines()]
        graph: List[Tuple[str, str]] = [(vertex[0], vertex[1]) for vertex in input_graph]

        # now add all those paths but backwards
        graph.extend([(target, start) for start, target in graph])

        success = []

        def part1_filter(target, current_path):
            return target.isupper() or target not in current_path

        find_all_paths(success, graph, ["start"], part1_filter)
        cleared = cleanup(success)
        paths_with_smaller_caves = [c for c in cleared if len([v for v in c[1:-1] if v.islower()])]
        print("part1", len(paths_with_smaller_caves))


        def part2_filter(target, current_path):
            lower = [v for v in current_path if v.islower()]
            is_small_duplicate = len(lower) != len(set(lower))
            return part1_filter(target, current_path) or (target != 'start' and not is_small_duplicate)

        find_all_paths(success, graph, ["start"], part2_filter)
        cleared = cleanup(success)
        paths_with_smaller_caves = [c for c in cleared if len([v for v in c[1:-1] if v.islower()])]
        print("part2", len(paths_with_smaller_caves))
