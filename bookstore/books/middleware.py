import logging

logger = logging.getlogger(__name__)

class LoggingMiddleware:
    def __init__(self,  get_response):
        self.get_responce = get_response

        def __call__(self, request):

          logger.info(f"Request Method: {request.method} | Request Path: {request.path}")

          response = self.get_response(request)
          return response


        



 