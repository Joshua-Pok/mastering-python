import os

def traverse(directory_path: str):
    res = []


    try:

        for directory in os.listdir(directory_path): #os.listdir gives us the names of files and folders inside
            full_path = os.path.join(directory_path, directory) # os.path.join ALWAYS returns a string
            if os.path.islink(full_path):
                continue
            if os.path.isfile(full_path):
                res.append(full_path)

            if os.path.isdir(full_path):
                res.extend(traverse(full_path))

    except PermissionError:
        print("Warning, skipping inaccesible path...")
        return res


    return res




