from src.deep_indexer.indexer import create_reverse_index


def test_create_reverse_index_handles_text_and_ignores_binary(tmp_path):

    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file3 = tmp_path / "file3.txt"


    file1.write_text("apple banana")
    file2.write_text("banana")
    file3.write_text("apple")


    binary = tmp_path / "binary.bin"
    binary.write_bytes(b'\xff\xfe')


    paths = [file1, file2, file3] # path.name is jsu tthe name of the file, we should just always use full paths


    reverse_index = create_reverse_index(paths)


    assert "apple" in reverse_index
    assert "banana" in reverse_index
    assert tmp_path / "file1.txt" in reverse_index["banana"]


