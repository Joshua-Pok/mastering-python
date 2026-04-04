import os

from src.deep_indexer.traversal import traverse

def test_traverse_discovers_all_files_and_ignores_symlinks(tmp_path): # tmp path is a argument built in pytest that provides temporary directory unique to this test invocation

    root = tmp_path / "root"

    # create root directory and subdirectories
    (root/"subdir").mkdir(parents=True, exist_ok=True)

    file_path = root / "subdir" / "filename.txt"
    file_path.write_text("hello world")



    os.symlink(root, root / "subdir" / "link_to_root")

    res = traverse(root)

    assert len(res) == 1


def test_traverse_survives_locked_directories(tmp_path):
    root = tmp_path / "root"


    accessible_file = root / "accessible_file.txt"

    (root/"locked_dir").mkdir(parents=True, exist_ok=True)

    hidden_file = root / "locked_dir" / "hidden_file.txt"


    (root/"open_dir").mkdir(parents=True, exist_ok=True)

    visible_file = root / "open_dir" / "visible_file.txt"

    # we need to write the text so the file actually exists
    accessible_file.write_text("accessible")
    hidden_file.write_text("hidden")
    visible_file.write_text("im visible!")

    os.chmod(root / "locked_dir", 0x000) # lock the locked dir


    results = traverse(root)

    assert str(accessible_file) in results
    assert str(visible_file) in results
    assert str(hidden_file) not in results

    




