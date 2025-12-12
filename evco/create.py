import argparse
from pathlib import Path
import shutil


def create(year: int, day: int, name: str):
    year_dir = Path.cwd().joinpath(str(year))
    year_md = year_dir.joinpath('README.md')
    if not year_dir.exists():
        year_dir.mkdir()
        template_init = Path.cwd().joinpath('evco/templates/init.py')
        dest_init = year_dir.joinpath('__init__.py')
        shutil.copy(str(template_init), str(dest_init))

        template_md = Path.cwd().joinpath('evco/templates/readme_year.md')
        shutil.copy(str(template_md), str(year_md))
        with open(str(year_md), mode='r+', encoding='utf-8') as f:
            contents = f.read().replace('<<year>>', str(year))
            f.seek(0)
            f.truncate(0)
            f.write(contents)
        

    quest_str = '{:02d}'.format(day)
    quest_dir = year_dir.joinpath(f'quest{quest_str}')
    if quest_dir.exists():
        raise Exception('Quest already exists')
    quest_dir.mkdir()

    with open(year_md, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        idx = next(i for i, x in enumerate(lines) if f'badge/{quest_str}' in x)
        lines[idx] = lines[idx].replace('gray', 'green').replace('%86', '%85')
        f.seek(0)
        f.writelines(lines)

    data_dir = quest_dir.joinpath('data')
    if not data_dir.exists():
        data_dir.mkdir()
    for i in range(1, 4):
        test_file = data_dir.joinpath(f'{i}_test.txt')
        with open(test_file, mode='w') as f: pass
        data_file = data_dir.joinpath(f'{i}.txt')
        with open(data_file, mode='w') as f: pass    

    template_py = Path.cwd().joinpath('evco/templates/py.py')
    py_file = f'{name}.py'
    dest_py = quest_dir.joinpath(py_file)
    shutil.copy(str(template_py), str(dest_py))

    template_md = Path.cwd().joinpath('evco/templates/readme_day.md')
    with open(str(template_md), mode='r') as f:
        day_contents = f.read().replace('<<year>>', str(year)).replace('<<quest>>', str(day)).replace('<<quest_str>>', quest_str)
        day_contents = day_contents.replace('<<name>>', py_file).replace('<<title>>', name.replace('_', ' ').title())
    with open(str(year_md), mode='a') as f:
        f.write(day_contents)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a new Advent of Code folder and associated files')
    parser.add_argument('-y', '--year', help='The year to place the new files under', required=True, type=int)
    parser.add_argument('-d', '--day', help='The day to place the new files under', required=True, type=int)
    parser.add_argument('-n', '--name', help='The name of the new file', required=True)
    args = vars(parser.parse_args())
    create(**args)
