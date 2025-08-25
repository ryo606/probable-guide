from memo_app import add_note, list_notes, clear_notes


def test_add_and_list(tmp_path):
    path = tmp_path / "notes.json"
    add_note("first", path)
    add_note("second", path)
    assert list_notes(path) == ["first", "second"]


def test_clear(tmp_path):
    path = tmp_path / "notes.json"
    add_note("note", path)
    clear_notes(path)
    assert list_notes(path) == []
