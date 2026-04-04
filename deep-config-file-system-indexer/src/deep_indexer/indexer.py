from typing import List
from pathlib import Path

def create_reverse_index(paths: List[Path]):


    reverse_idx = {} # create locally

    for path in paths:

        with open(path, "r", encoding='utf-8') as f:
            try:
                contents = f.read()
            except UnicodeDecodeError as e:
                print(e)
                continue


            tokens = contents.split() # split into individual words
            token_set = set(tokens)


            for token in token_set:
                if token in reverse_idx:
                    reverse_idx[token].append(path)

                else:

                    reverse_idx[token] = [path]

    return reverse_idx

