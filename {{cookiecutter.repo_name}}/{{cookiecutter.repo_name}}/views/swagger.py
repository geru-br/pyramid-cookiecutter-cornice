import colander
from cornice import Service
from cornice.service import get_services
from cornice_swagger.converters.schema import (NumberTypeConverter,
                                               StringTypeConverter)
from cornice_swagger.swagger import CorniceSwagger
from pyramid.view import view_config

swagger = Service(name='swagger-api', path='/__api__', description="CBGB API documentation")


def _define_security_section(swagger, service, method):
    return []


def _get_services():
    return [service for service in get_services() if service.name not in ['health', 'swagger-api']]


def _openAPI_spec():
    swagger = {
        'info': {
            'description': '{{cookiecutter.project_name}} RestAPI.'
        },
    }

    CorniceSwagger.default_type_converter = StringTypeConverter

    CorniceSwagger.custom_type_converters = {
        colander.Decimal: NumberTypeConverter
    }

    CorniceSwagger.default_security = _define_security_section

    generator = CorniceSwagger(_get_services())

    spec = generator('{{cookiecutter.project_name}} API', '1.0.0', swagger=swagger)

    return spec


@swagger.get()
def openAPI_spec(request):
    return _openAPI_spec()



@view_config(route_name='apidocs', renderer='templates/swagger.jinja2')
def apidocs(request):
    return {}