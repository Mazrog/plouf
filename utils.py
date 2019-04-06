import os

def get_cwd():
    return os.getcwd()

def get_dirname():
    return os.path.basename(get_cwd())

def get_file_path(filename):
    cwd = get_cwd()
    return os.path.join(cwd, filename)

def file_exists(filename):
    f = get_file_path(filename)
    return os.path.exists(f)

def mkdirp(dirs):
    if not isinstance(dirs, list):
        mkdirp([dirs])
    else:
        for d in dirs:
            os.makedirs(d, exist_ok=True)

