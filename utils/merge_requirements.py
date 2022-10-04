from pathlib import Path

# Get all the requirements.txt files from the subfolders of the current folder

def get_requirements_files() -> list[str]:
    return list(Path().glob('**/requirements.txt'))


def merge_requirements(files: list[str]) -> set[str]:
    requirements = set()
    for file in files:
        requirements.update(file.read_text().splitlines())
    return requirements


def write_requirements(requirements: set[str]) -> None:
    Path('requirements.txt').write_text('\n'.join(sorted(requirements)))


if __name__ == '__main__':
    files = get_requirements_files()
    requirements = merge_requirements(files)
    write_requirements(requirements)