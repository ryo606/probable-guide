import json
from pathlib import Path

DEFAULT_PATH = Path("notes.json")


def load_notes(path: Path | str = DEFAULT_PATH) -> list[str]:
    """Load notes from *path*.

    Returns an empty list if the file does not exist.
    """
    path = Path(path)
    if path.exists():
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    return []


def save_notes(notes: list[str], path: Path | str = DEFAULT_PATH) -> None:
    """Persist *notes* to *path* in JSON format."""
    path = Path(path)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(notes, fh, ensure_ascii=False, indent=2)


def add_note(text: str, path: Path | str = DEFAULT_PATH) -> None:
    """Append *text* as a new note in *path*."""
    notes = load_notes(path)
    notes.append(text)
    save_notes(notes, path)


def list_notes(path: Path | str = DEFAULT_PATH) -> list[str]:
    """Return all notes stored at *path*."""
    return load_notes(path)


def clear_notes(path: Path | str = DEFAULT_PATH) -> None:
    """Remove all notes stored at *path*."""
    save_notes([], path)


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Simple memo app")
    parser.add_argument("command", choices=["add", "list", "clear"], help="Action to perform")
    parser.add_argument("text", nargs="?", help="Text of the note when adding")
    parser.add_argument("--path", default=str(DEFAULT_PATH), help="Path to notes file")

    args = parser.parse_args()
    path = Path(args.path)

    if args.command == "add":
        if args.text is None:
            parser.error("add command requires text")
        add_note(args.text, path)
    elif args.command == "list":
        for idx, note in enumerate(list_notes(path), 1):
            print(f"{idx}. {note}")
    elif args.command == "clear":
        clear_notes(path)


if __name__ == "__main__":
    main()
