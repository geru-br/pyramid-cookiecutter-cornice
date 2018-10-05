import click
import logging
from pyramid.settings import asbool
import sys
from pyramid.paster import bootstrap
from .swagger import swagger


@click.group()
@click.argument('config_uri')
@click.option('-d', '--debug', envvar='DEGUG', default=None)
@click.option('-s', '--silent', default=None)
def cli(config_uri, debug=None, silent=None):

    if not asbool(silent):

        root = logging.getLogger()

        if debug:
            root.setLevel(logging.DEBUG)
        else:
            root.setLevel(logging.INFO)

        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        ch.setFormatter(formatter)
        root.addHandler(ch)

        if debug:
            logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

    bootstrap(config_uri)


cli.add_command(swagger)


if __name__ == '__main__':
    cli()
