from pathlib import Path
from typing import Generator


def return_md_files(dir: Path) -> Generator[Path, None, None]:
    files = dir.glob("*.md")
    for file in files:
        yield file


def get_data(file: Path) -> list[str]:
    with file.open("r") as f:
        data = f.readlines()
        return data


def redux(data: list[str]) -> str:
    hyphens = [i for i, x in enumerate(data) if x == "---\n"]
    # If it does not hyphens it will be because the properties are not set, which means that the file does not need to be cleanes
    if not hyphens:
        return ""
    header = data[hyphens[0] : hyphens[-1] + 1]

    tags = [i for i in header if " -" in i]

    # Headings
    body = data[hyphens[-1] + 1 :]
    headings = [i for i, x in enumerate(body) if x[0] == "#" and x[1] == " "]
    if headings:
        for heading in reversed(headings):
            del body[heading]
    # Tags
    body.append("\n### Tags:\n")
    for tag in tags:
        body.append(tag)

    return "".join(body)


def write_data(content: str, file: Path) -> None:
    with file.open("w") as f:
        f.write(content)


def logger(file: Path) -> None:
    log_file = file.parent.parent / "logg_file.txt"
    print(log_file)

    with log_file.open("a") as f:
        f.write(f"{file.name}\n")


def main() -> None:
    path = Path("./0 NOTAS ATOMICAS/")
    for file in return_md_files(path):
        content = get_data(file)
        new_content = redux(content)
        if not new_content:
            logger(file)
            continue
        else:
            write_data(new_content, file)


if __name__ == "__main__":
    main()
