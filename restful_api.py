import nest
import logging

from sys import stdout
from logging import StreamHandler
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_basicauth import BasicAuth


app = Flask(__name__)
api = Api(app)
app.config['BASIC_AUTH_USERNAME'] = 'john'
app.config['BASIC_AUTH_PASSWORD'] = 'matrix'
basic_auth = BasicAuth(app)


class RestfulAPI(Resource):
    method_decorators = {
        'post': [basic_auth.required]
    }

    def post(self):
        input_json = request.get_json()
        json_data = input_json['data']
        nesting_order = input_json['hierarchy']

        if json_data is not None:
            extra_keys = nest.get_extra_keys_list(nesting_order, json_data)
            response = nest.regroup_json_data(json_data, nesting_order, extra_keys)
            return jsonify(response)
        else:
            app.logger.error('ERROR 400 - No JSON data provided by user, cannot serve GET response.')
            response = {
                'status': '400',
                'message': 'No input JSON was provided, please use POST request to pass JSON to the /api endpoint.'
            }
            return jsonify(response)


api.add_resource(RestfulAPI, '/api', endpoint='api')

if __name__ == '__main__':
    handler = RotatingFileHandler(filename='test_rest_api.log', maxBytes=10000, backupCount=1)
    stream_handler = StreamHandler(stdout)
    handler.setLevel(logging.DEBUG)
    stream_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)  # To log to a rotating file.
    app.logger.addHandler(stream_handler)  # To log to stdout.
    app.run(debug=True)
