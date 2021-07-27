from flask import Response, jsonify, request
from . import api

@api.route("/")
def index():
    return Response("Hello, world!", status=200)


@api.route("/custom", methods=["POST"])
def custom():
    payload = request.get_json()

    if payload.get("say_hello") is True:
        output = jsonify({"message": "Hello!"})
    else:
        output = jsonify({"message": "..."})

    return output
