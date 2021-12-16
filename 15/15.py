import queue
from dataclasses import dataclass

# input = "sample.txt"
input = "input.txt"

"""
The solution is applying Dijkstra algorithm, with risk factor as length
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
we calculate the map of cummulative risks and traverse the path of lowest risk. 
Optimization can be done by selecting fields with lowest risk first (reminds of A* algorithm)
"""


@dataclass
class Point:
    x: int
    y: int
    autorisk: int = 0
    entry = None
    risk = 99999999

    def __lt__(self, other):
        return self.risk < other.risk

    def __hash__(self):
        return self.x+self.y

    def __str__(self):
        return f"Point({self.x},{self.y}, risk={self.risk})"

if __name__ == "__main__":
    with open(input, "r") as r:
        danger_map = [[Point(x, y, int(risk)) for x, risk in enumerate(f.rstrip())] for y, f in enumerate(r.readlines())]

    y_max = len(danger_map) - 1
    x_max = len(danger_map[0]) - 1


    def get_adj_fields(x, y):
        for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            ey = y + dy
            ex = x + dx
            if 0 <= ey <= y_max and 0 <= ex <= x_max:
                yield Point(ex, ey)


    def get_effective_adj(p: Point):
        for c in get_adj_fields(p.x, p.y):
            yield danger_map[c.y][c.x]


    def calculate_lowest_risk_entry():
        end = danger_map[y_max][x_max]
        origin = danger_map[0][0]
        origin.risk = origin.autorisk
        unsure = queue.PriorityQueue()
        sure = set()

        unsure.put(danger_map[origin.y][origin.x])
        while not unsure.empty():
            candidate:Point = unsure.get()
            if candidate in sure:
                continue
            sure.add(candidate)
            if candidate == end:
                break

            adjs = [x for x in get_effective_adj(candidate)]
            for a in adjs:
                if a.entry is None or a.risk > a.autorisk + candidate.risk:
                    a.entry = candidate
                    a.risk = a.autorisk + candidate.risk
            adjs = sorted(adjs)
            for a in adjs:
                if a not in sure:
                    unsure.put(a)
    calculate_lowest_risk_entry()

    print("Cummulated risk calculated", danger_map[y_max][x_max].risk-1)
