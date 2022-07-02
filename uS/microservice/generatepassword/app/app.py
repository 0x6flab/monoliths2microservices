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


class GeneratePassword(Resource):
    def get(self):
        do_task(3)
        password = ''.join(random.choice(string.printable) for i in range(16))
        return encode_responses(password)

api.add_resource(GeneratePassword, '/g')

if __name__ == '__main__':
    app.run(debug=True, port=5054, host="0.0.0.0")
