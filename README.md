# Plouf

Setup
```sh
$ git clone https://github.com/Mazrog/plouf
$ pip install --user plouf
```

Enbale bash autocompletion
```sh
$ eval "$(_PLOUF_COMPLETE=source plouf)"
```

Start using plouf!

*Do not forget the `--help` flag in case you want some details on the fly*

`plouf`

- `init`: goes through some prompts to initialize the project's repository
- `add [library|exec]`: for now just know two configurations, used to add such projects
- `setup`: builds all the folders and creates the startup files with the templates
    - `-o, --override` [default=`False`] if files already exist, rewrite them

