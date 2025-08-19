from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, Throttled) and response is not None:
        response.data = {
            "error": "Too many requests, please slow down.",
            "available_in": f"{exc.wait} seconds",
        }
    return response
