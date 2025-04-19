from pathlib import Path

def getContent(path: Path) -> tuple[list[str], list[str]]:
    entries = ([], [])
    for entry in path.iterdir():
        dest = 0 if entry.is_dir() else 1
        entries[dest].append(entry)
    return entries


def moveFiles(entries: tuple, dest: dict) -> None:
    entries = entries
    dest = dest
    pass


def readConfig(config: Path) -> dict:
    config = config
    return {}


print(getContent(Path('/home/darth/Downloads/')))
