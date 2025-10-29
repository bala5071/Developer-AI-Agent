import os

def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)
    return f"File {path} created."

def read_file(path):
    with open(path, "r") as f:
        return f.read()
