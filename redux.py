from pathlib import Path
from typing import Generator


def return_md_files(dir: Path) -> Generator[Path, None, None]:
    files = list(dir.glob("*.md"))
    for file in files:
        yield file


path = Path("./0 NOTAS ATOMICAS/")

for i in return_md_files(path):
    print(i.name)
