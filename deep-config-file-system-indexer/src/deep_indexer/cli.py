import json
import sys
import os
import argparse

from src.deep_indexer.indexer import create_reverse_index
from src.deep_indexer.traversal import traverse


def build_index(target_dir, output_path):

    print("Starting traversal...")

    file_list = traverse(target_dir)


    print(f"found {len(file_list)} files, Starting indexer...")

    index = create_reverse_index(file_list)


    try:
        with open(output_path, "w", encoding='utf-8') as f:
            json.dump(index, f, indent=2)
    except PermissionError as e:
        print(e)


def main():
    parser = argparse.ArgumentParser()


    parser.add_argument("target_dir", help="target directory to comb and build index")

    parser.add_argument("--output", help="optional target output, default: index.json", default="index.json")


    args = parser.parse_args()
    target_dir = args.target_dir
    output_path = args.output


    if not os.path.isdir(target_dir):
        print("Error, target dir is not a dir")
        sys.exit(1)


    build_index(target_dir, output_path)


if __name__ == "__main__":
    main()







