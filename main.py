from pathlib import Path
from yaml import safe_load
from shutil import move
from sys import argv
from getopt import getopt

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
    try:
        with open(config, 'r') as config_file:
            return safe_load(config_file)
    except FileNotFoundError:
        print("\nConfiguration file not found.\n")
        quit(1)


def getConfig(opts) -> Path:
    config_path = './config.yaml'
    for opt, arg in opts:
        if opt in ("c", "--config"):
            config_path = Path(arg)
    return Path(config_path)


def main() -> None:
    opts, args = getopt(argv[1:], "c:", ["config"])
    config_path = getConfig(opts)
    config = readConfig(config_path)
    content = getContent(Path(config['source']))
    moveFiles(content, config)
    print("Files moved!")


if __name__ == '__main__':
    main()
