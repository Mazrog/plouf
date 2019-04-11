# Plouf

Little CLI tools written in python, that lets you manage and organize quicky a folder/project structure.

## Setup

From sources for now, maybe a pip package soon?

```sh
$ git clone https://github.com/Mazrog/plouf

# Compiling package
$ python3 setup.py bdist_wheelrunning bdist_wheel

# Actually installing
$ pip3 install --user plouf/dist/plouf-0.1-py3-none-any.whl
```

*Note: The `--user` parameter is optional, it is just of you want to perform a local installation, without `sudo` permissions*

Enable bash autocompletion (if disabled)
```sh
$ eval "$(_PLOUF_COMPLETE=source plouf)"
```

## Start using plouf!

*Do not forget the `--help` flag in case you want some details on the fly*

`plouf`

- `init`: goes through some prompts to initialize the project's repository
- `add [library|exec]`: for now just know two configurations, used to add such projects
- `setup`: builds all the folders and creates the startup files with the templates
    - `-o, --override` [default=`False`] if files already exist, rewrite them

## Roadmap, aka dreams (unsorted):

- adding some dependency management, npm-style?
- user-defined projet types and templates (in a `.plouftemplates` file at the root of directory)
- user-defined tests frameworks (ie other than just `doctest`)
- maybe some git linkage?
- [Utils]: better handling of exceptions
