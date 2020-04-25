from flask import Flask, jsonify, request
from flask_restful import Resource
from flask_restful import Api


host_addr = "0.0.0.0"
host_port = 8080


class ThingworxResultImg(Resource):
    @staticmethod
    def get():
        try:

            return jsonify("hello I'm server :) ")
        except Exception as e:
            return {'error': str(e)}


app = Flask('Jenkins 실습 서버')
api = Api(app)

api.add_resource(ThingworxResultImg, '/hello')


if __name__ == '__main__':
    app.run(host=host_addr,
            port=host_port)
