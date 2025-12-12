import evco
from collections import Counter
import itertools


Dancers = list[list[int]]

def parse_dancers(data: str) -> Dancers:
    dancers = [list(map(int, x.split())) for x in evco.read_lines(data)]
    return list(map(list, zip(*dancers)))

def perform_round(columns: Dancers, round: int) -> Dancers:
    source_col = round % len(columns)
    target_col = columns[(source_col + 1) % len(columns)]
    clapper = columns[source_col].pop(0)
    target_len = len(target_col)

    position = (clapper - 1) % (2*target_len)
    if position >= target_len:
        position = 2*target_len - position
    target_col.insert(position, clapper)
    return columns

def shout(columns: Dancers) -> int:
    return int(''.join(str(x[0]) for x in columns))

def save(dancers: Dancers) -> tuple[tuple[int]]:
    return tuple(map(tuple, dancers))


@evco.register(__file__, 1)
def part_one(data: str):
    dancers = parse_dancers(data)
    for i in range(10):
        dancers = perform_round(dancers, i)
    return shout(dancers)

@evco.register(__file__, 2)
def part_two(data: str):
    dancers = parse_dancers(data)
    counter, round, result = Counter(), 0, 0
    while counter[result] < 2024:
        dancers = perform_round(dancers, round)
        result = shout(dancers)
        counter[result] += 1
        round += 1
    return result * round

@evco.register(__file__, 3)
def part_three(data: str):
    dancers = parse_dancers(data)
    visited = set()
    highest_shout = shout(dancers)
    for round in itertools.cycle(range(4)):
        if (state := (round, save(dancers))) in visited:
            break
        visited.add(state)
        dancers = perform_round(dancers, round)
        highest_shout = max(highest_shout, shout(dancers))
    return highest_shout

if __name__ == '__main__':
    evco.run(test=False)
