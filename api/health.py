from flask import Response
from . import api

@api.route("/health")
def health():
    return Response("OK", status=200)
