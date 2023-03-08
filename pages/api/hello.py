from flask import Flask
from flask_restful import reqparse, Api, Resource
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')


class Message(Resource):
    def get(self):
        response_body = {
            "name": "Responder",
            "message": "Hello World!"
        }
        return response_body


api.add_resource(Message, '/api/hello')

if __name__ == '__main__':
    app.run(debug=True)