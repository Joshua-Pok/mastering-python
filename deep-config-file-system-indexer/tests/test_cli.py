


import json

from src.deep_indexer.cli import build_index

def test_build_index_orchestrates_and_saves_json(tmp_path):
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()

    test_file = test_dir / "test_file.txt"


    test_file.write_text("Hello World!")


    output_path = test_dir / "output.json"


    build_index(test_dir, output_path)


    assert(output_path.exists())

    try:
        with open(output_path, "r") as f:
            index = json.load(f)
            assert "Hello" in index
    
    except PermissionError as e:
        print(e)


def test_cli_rejects_files_and_accepts_directories(tmp_path):
    valid_dir = tmp_path / "valid"
    valid_dir.mkdir()


    invalid_file = tmp_path / "invalid.txt"
    invalid_file.write_text("I am invalid!")







