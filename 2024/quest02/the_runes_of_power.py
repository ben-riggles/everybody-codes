import evco
import regex as re
from typing import Generator


def parse_input(data: str, reverse=False) -> tuple[set[str], str]:
    runic_words, inscription = evco.read_chunks(data)
    runic_words = {x.strip() for x in runic_words.split(':')[1].split(',')}
    if reverse:
        runic_words |= {word[::-1] for word in runic_words}
    return runic_words, inscription

def pattern(runic_words: set[str]):
    words = sorted(runic_words, key=lambda x: len(x), reverse=True)
    return re.compile(rf'({'|'.join(word for word in words)})')

def find_runic_words(search_str: str, regex: str) -> Generator[int]:
    for i in re.finditer(regex, search_str, overlapped=True):
        yield from range(i.start(), i.end())


@evco.register(__file__, 1)
def part_one(data: str):
    runic_words, inscription = parse_input(data)
    return sum(inscription.count(word) for word in runic_words)

@evco.register(__file__, 2)
def part_two(data: str):
    runic_words, inscription = parse_input(data, reverse=True)
    regex = pattern(runic_words)

    symbols = set(find_runic_words(inscription, regex))
    return len(symbols)

@evco.register(__file__, 3)
def part_three(data: str):
    runic_words, inscription = parse_input(data, reverse=True)
    regex = pattern(runic_words)

    rows = inscription.split('\n')
    columns = [''.join(x) for x in zip(*rows)]
    size = len(rows[0])
    
    horizontal = {(c % size, r) for r, row in enumerate(rows) for c in find_runic_words(row + row, regex)}
    vertical = {(c, r) for c, col in enumerate(columns) for r in find_runic_words(col, regex)}
    scales = horizontal | vertical
    return len(scales)

if __name__ == '__main__':
    evco.run(test=False)
