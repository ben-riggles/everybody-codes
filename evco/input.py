from pathlib import Path


# DATA_FILE = None
# def set_data_file(filename):
#     global DATA_FILE
#     DATA_FILE = filename

# def _data_file(filename) -> str:
#     return str(Path(DATA_FILE).parent.joinpath(f'{filename}.txt'))

def read_data(_file) -> str:
    with open(_file) as f:
        data = f.read()
    return data

def read_lines(_file) -> list[str]:
    with open(_file) as f:
        data = f.read().splitlines()
    return data

def read_chunks(_file) -> list[str]:
    with open(_file) as f:
        data = f.read().split('\n\n')
    return data

def read_grid(_file) -> list[list[str]]:
    with open(_file) as f:
        data = list(map(list, f.read().splitlines()))
    return data
