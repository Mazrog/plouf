import os

def get_dirname():
    return os.path.basename(os.getcwd())

def get_file_path(filename):
    cwd = os.getcwd()
    return os.path.join(cwd, filename)

def file_exists(filename):
    f = get_file_path(filename)
    return os.path.exists(f)

