
import json
import click
import json
from {{ cookiecutter.project_name }}.swagger import _openAPI_spec

@click.group()
def swagger():
    pass


@swagger.command(name='extract')
def extract():
    print(json.dumps(_openAPI_spec()))