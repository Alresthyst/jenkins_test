from flask import Flask, jsonify
from flask_restful import Resource
from flask_restful import Api
from optparse import OptionParser
import sys
import os
import yaml


parser = OptionParser()
parser.add_option("-f", "--file_name", dest="file_name", help="IP setting",
                  default="release_config.yml")
(options, args) = parser.parse_args(sys.argv)

config_file_name = options.file_name
config_content = yaml.full_load(open(os.path.join(os.getcwd(), config_file_name)))

host_addr = config_content['host_address']
host_port = config_content['host_port']


class ThingworxResultImg(Resource):
    @staticmethod
    def get():
        try:

            return jsonify("hello I'm " + config_content['name'] + " :)")
        except Exception as e:
            return {'error': str(e)}


app = Flask('Jenkins 실습 서버')
api = Api(app)

api.add_resource(ThingworxResultImg, '/hello')


if __name__ == '__main__':
    print("\n"*3, "="*100, "\n")
    print("Hello! I'm " + config_content['name'] + " ^^\n")
    app.run(host=host_addr,
            port=host_port)
