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


class Capitalize(Resource):
    def get(self, capsText):
        do_task(1)
        return encode_responses(capsText.capitalize())

class LowerCase(Resource):
    def get(self, capsText):
        do_task(1)
        return encode_responses(capsText.lower())

class UpperCase(Resource):
    def get(self, capsText):
        do_task(1)
        return encode_responses(capsText.upper())
    
class SwapCase(Resource):
    def get(self, capsText):
        do_task(1)
        return encode_responses(capsText.swapcase())
    
class TitleCase(Resource):
    def get(self, capsText):
        do_task(1)
        return encode_responses(capsText.title())

class CheckUpperCase(Resource):
    def get(self, capsText):
        do_task(2)
        return encode_responses(capsText.isupper())

class CheckLowerCase(Resource):
    def get(self, capsText):
        do_task(2)
        return encode_responses(capsText.islower())

class GeneratePassword(Resource):
    def get(self):
        do_task(3)
        password = ''.join(random.choice(string.printable) for i in range(16))
        return encode_responses(password)

api.add_resource(Capitalize, '/c/<capsText>')
api.add_resource(LowerCase, '/l/<capsText>')
api.add_resource(UpperCase, '/u/<capsText>')
api.add_resource(SwapCase, '/s/<capsText>')
api.add_resource(TitleCase, '/t/<capsText>')
api.add_resource(CheckUpperCase, '/cu/<capsText>')
api.add_resource(CheckLowerCase, '/cl/<capsText>')
api.add_resource(GeneratePassword, '/g')

if __name__ == '__main__':
    app.run(debug=True, port=5050, host="0.0.0.0")
