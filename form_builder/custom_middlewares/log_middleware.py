import logging, time

request_logger = logging.getLogger("middleware")


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if len(request.body) > 200:
            self._initial_http_body = request.body[:200]
        else:
            self._initial_http_body = request.body
        self.start_time = time.time()
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        total_second = round(time.time() - self.start_time, 2)
        if request.path.startswith("/api/"):
            request_logger.log(
                logging.INFO,
                f"[{total_second}-sec.] {request.method} {request.path}\n{request.GET}\nBODY: {self._initial_http_body}\nPOST: {request.POST}\n{response.status_code}.",
            )
        return response
