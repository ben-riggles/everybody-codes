import evco
from evco.grid import KeyGrid
from evco.utils import adjacent_points


class MiningMap(KeyGrid):
    fields = {
        'diggable': '#'
    }

    def digs(self, diagonal: bool = False) -> int:
        diggable = self['diggable']
        digs = len(diggable)
        while diggable:
            new_digs = {p for p in diggable if set(adjacent_points(p, diagonal)) < diggable}
            digs += len(new_digs)
            diggable = new_digs
        return digs


@evco.register(__file__, 1)
def part_one(data: str):
    mining_map = MiningMap(evco.read_data(data))
    return mining_map.digs()

@evco.register(__file__, 2)
def part_two(data: str):
    mining_map = MiningMap(evco.read_data(data))
    return mining_map.digs()

@evco.register(__file__, 3)
def part_three(data: str):
    mining_map = MiningMap(evco.read_data(data))
    return mining_map.digs(diagonal=True)

if __name__ == '__main__':
    evco.run(test=False)
