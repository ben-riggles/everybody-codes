import evco


def swings(nails: tuple[int], target: int, white_dots: bool = False) -> int:
    if white_dots:
        return sum(abs(x-target) for x in nails)
    return sum(x - target for x in nails)


@evco.register(__file__, 1)
def part_one(data: str):
    nails = tuple(map(int, evco.read_lines(data)))
    return swings(nails, min(nails))

@evco.register(__file__, 2)
def part_two(data: str):
    nails = tuple(map(int, evco.read_lines(data)))
    return swings(nails, min(nails))

@evco.register(__file__, 3)
def part_three(data: str):
    nails = tuple(map(int, evco.read_lines(data)))
    left, right = min(nails), max(nails)
    while True:
        target = (left + right) // 2
        prev = swings(nails, target-1, white_dots=True)
        current = swings(nails, target, white_dots=True)
        next = swings(nails, target+1, white_dots=True)

        if prev < current < next:
            right = target - 1
        elif prev > current > next:
            left = target + 1
        else:
            return current

if __name__ == '__main__':
    evco.run(test=False)
