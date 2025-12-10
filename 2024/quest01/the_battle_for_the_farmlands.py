import evco
from evco.utils import iter_groups, MultiValueEnum
from collections import Counter


class Creature(MultiValueEnum):
    Empty = 'x', None
    AncientAnt = 'A', 0
    BadassBeatle = 'B', 1
    CreepyCockroach = 'C', 3
    DiabolicalDragonfly = 'D', 5
    
    @property
    def potions(self) -> int:
        return self[1]


def battle(*creatures: Creature) -> int:
    creatures = tuple(x for x in creatures if x != Creature.Empty)
    count = len(creatures)
    return (count-1) * count + sum(x.potions for x in creatures)


@evco.register(__file__, 1)
def part_one(data: str):
    battles = Counter(evco.read_data(data))
    return sum(n * battle(Creature(k)) for k, n in battles.items())

@evco.register(__file__, 2)
def part_two(data: str):
    battles = Counter(iter_groups(evco.read_data(data)))
    return sum(n * battle(*(Creature(x) for x in k)) for k, n in battles.items())

@evco.register(__file__, 3)
def part_three(data: str):
    battles = Counter(iter_groups(evco.read_data(data), n=3))
    return sum(n * battle(*(Creature(x) for x in k)) for k, n in battles.items())

if __name__ == '__main__':
    evco.run(test=False)
