import evco


@evco.register(__file__, 1)
def part_one(data: str):
    pass

@evco.register(__file__, 2)
def part_two(data: str):
    pass

@evco.register(__file__, 3)
def part_three(data: str):
    pass

if __name__ == '__main__':
    evco.run(test=True)
