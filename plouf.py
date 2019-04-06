import click
import json
import os
import urllib.request

import utils
import templates

# define plouffile name -- constant
plouffile = ".plouffile"

tests_frameworks = {
    'doctest': 'https://raw.githubusercontent.com/onqtam/doctest/master/doctest/doctest.h',
    'catch': 'https://github.com/catchorg/Catch2/releases/latest/download/catch.hpp'
}

# Helper functions
def get_pf_path():
    """
    Returns plouffile full path
    """
    return utils.get_file_path(plouffile)

def valid_repo():
    """
    Returns boolean if current repository has already been initialized.
    """
    return os.path.exists(get_pf_path())

def make_structure(target_name, what, add_tests):
    """
    Depending on the target type what, creates the folder structure.
    """
    basepath = utils.get_file_path(target_name)
    paths = [ basepath ]
    if add_tests:
        paths += [
            utils.get_file_path("extern"),
            os.path.join(basepath, "tests")
        ]
    
    rel_paths = []
    if what == "exec":
        rel_paths = [
            os.path.join(target_name, "sample"),
            os.path.join(target_name, "src")
            ]
    elif what == "library":
        rel_paths = [
            os.path.join(target_name, "include", target_name),
            os.path.join(target_name, "src")
        ]
    
    paths += [ utils.get_file_path(k) for k in rel_paths ]

    utils.mkdirp(paths)

# Actual script

@click.group()
def main():
    """
    CLI tools for project creation.
    """
    pass

@main.command()
def init():
    """
    Initialize plouf project for this repository, creating plouffile.
    """

    if utils.file_exists(plouffile):
        click.confirm('A \"%s\" has been found in this repository, override it?' % plouffile, abort=True, prompt_suffix='')

    data = {
        'name': click.prompt('project name', default=utils.get_dirname()),
        'description': click.prompt('description', default=''),
        'author': click.prompt('author', default=''),
        'version': click.prompt('version', default='0.1.0')
    }

    click.echo(json.dumps(data, indent=2))
    click.confirm('Is this ok?', default=True, abort=True)
    
    try:
        with open(utils.get_file_path(plouffile), 'w') as pf:
            json.dump(data, pf, indent=4)
        
        click.echo(
            click.style('[SUCESS] ', fg="green") + 'Initialized empty plouf repository.'
        )

    except Exception as e:
        click.echo(
            click.style(e, fg="red"),
            err=True
        )

    pass


@main.command()
def setup():
    """
    Setup repository according to the plouffile.
    """
    if not valid_repo():
        click.echo(
            click.style('[FAILURE]', fg='red') + 'Not a plouf repository. (No \'.plouffile\' file found.)'
        )
        return
    

    pass


@main.command()
@click.argument('what', type=click.Choice(['library', 'exec']))
def add(what):
    """
    Adding an executable, library or test project.
    """
    if not valid_repo():
        click.echo(
            click.style('[FAILURE]', fg='red') + 'Not a plouf repository. (No \'.plouffile\' file found.)'
        )
        return

    try:
        data = {}
        name = click.prompt('%s name' % what, type=click.STRING)

        with open(get_pf_path(), 'r') as pf:
            data = json.load(pf)

        if not "projects" in data:
            data["projects"] = {}
        
        if name in data["projects"]:
            click.echo(
                click.style('[WARNING] ', fg="yellow") + 'A project with this name already exists.'
            )
            click.confirm('Do you want to override it', prompt_suffix='?', abort=True)
        
        add_tests = click.confirm('create tests', prompt_suffix='?', default=True)
        if add_tests:
            f_name = click.prompt('test framework', type=click.STRING, default='doctest')
            f_url = click.prompt('header url', type=click.STRING, default=tests_frameworks[f_name])

            data.setdefault("tests", {})[f_name] = f_url

        data["projects"][name] = { "type": what }

        make_structure(name, what, add_tests)

        with open(get_pf_path(), 'w') as pf:
            json.dump(data, pf, indent=4)
        
        click.echo(
            click.style('[SUCESS] ', fg="green") + 'Project added successfully.'
        )

    except Exception as e:
        click.echo(
            click.style(e, fg="red"),
            err=True
        )

    pass

