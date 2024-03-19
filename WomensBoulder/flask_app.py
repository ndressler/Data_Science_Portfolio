# file app.py
from flask import Flask
from flask_restful import Api
from data_loader import load_data
from data_resources import DataListResource, DataResource

app = Flask(__name__)
api = Api(app)
data = load_data()

# Registering resources with Flask-RESTful
api.add_resource(DataListResource, '/api/data', resource_class_args=(data,))
api.add_resource(DataResource, '/api/data/<int:id>', '/api/data/competition/<string:competition>',
                 '/api/data/city/<string:city>', '/api/data/year/<int:year>',
                 '/api/data/dates/<string:dates>', '/api/data/rank/<string:rank>',
                 '/api/data/name/<string:name>', '/api/data/surname/<string:surname>',
                 '/api/data/country/<string:country>', resource_class_args=(data,))

if __name__ == '__main__':
    app.run(debug=True)
