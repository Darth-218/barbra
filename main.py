from pathlib import Path
from yaml import safe_load
from shutil import move

def getContent(path: Path) -> tuple[list[str], list[str]]:
    entries = ([], [])
    for entry in path.iterdir():
        dest = 1 if entry.is_dir() else 0
        entries[dest].append(entry)
    return entries


def moveFiles(entries: tuple, dest: dict) -> None:
    file: Path
    for file in entries[0]:
        try:
            move(file, dest[file.as_posix().split(".")[-1]])
        except KeyError:
            move(file, dest['other'])
    for directory in entries[1]:
        move(directory, dest['directory'])


def readConfig(config: Path) -> dict:
    with open(config, 'r') as config_file:
        return safe_load(config_file)


if __name__ == '__main__':
    config_path = Path('./config.yaml')
    config = readConfig(config_path)
    content = getContent(Path(config['source']))
    moveFiles(content, config)
    print("Files moved!")
