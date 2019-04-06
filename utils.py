import os

def get_dirname():
    return os.path.basename(os.getcwd())

def file_exists(filename):
    cwd = os.getcwd()
    f = os.path.join(cwd, filename)
    return os.path.exists(f)


