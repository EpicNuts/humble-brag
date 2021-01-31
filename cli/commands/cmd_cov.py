import subprocess

import click


@click.command()
@click.argument('path', default='humble_brag')
def cli(path):
    """
    Run a test coverage report.

    :param path: Test coverage path
    :return: Subprocess call result
    """

    cmd = f'py.test {path}'
    return subprocess.call(cmd, shell=True)
