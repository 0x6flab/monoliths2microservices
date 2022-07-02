import random, string, time
from flask import Flask, jsonify
from flask_restful import Resource,Api, reqparse

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api=Api(app)

def do_task(timer):
    time.sleep(timer)


def encode_responses(data):
    return jsonify({"response": data})


class SwapCase(Resource):
    def get(self, capsText):
        do_task(1)
        return encode_responses(capsText.swapcase())
    


api.add_resource(SwapCase, '/s/<capsText>')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
