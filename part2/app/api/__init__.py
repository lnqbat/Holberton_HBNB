from flask_restx import Api # type: ignore
from flask import Blueprint

from app.api.v1.users import api as users_api
from app.api.v1.places import api as places_api
from app.api.v1.reviews import api as reviews_api
from app.api.v1.amenities import api as amenities_api

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint, title='HBnB API', version='1.0', description='HBnB REST API')

api.add_namespace(users_api, path='/users')
api.add_namespace(places_api, path='/places')
api.add_namespace(reviews_api, path='/reviews')
api.add_namespace(amenities_api, path='/amenities')
