import click
import json
import os

import utils

# define plouffile name -- constant
plouffile = ".plouffile"

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
    
    # process

    click.echo('Initialized empty plouf repository.')

    pass


@main.command()
def setup():
    """
    Setup repository according to the plouffile.
    """
    pass


@main.command()
def deploy():
    """
    Builds and deploy projects
    """
    pass

@main.command()
def add():
    """
    Adding an executable, library or test project.
    """
    pass