import logging
from datetime import datetime



class LoggerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        logging.basicConfig(filename="stdout.log", level=logging.INFO)

    def __call__(self, request):
        """логирую дата и время события, запрошенный URL, HTTP метод. """

        import locale
        locale.setlocale(locale.LC_TIME, "ru_RU")
        """ “service”: name, “message”: string1, “error”: string2 or nil, “endpoint”: string3};"""
        logging.info({"дата: {}, время: {}, запрошенный URL: {}, HTTP метод: {}".format(
            datetime.today().strftime('%d-%m-%Y'),
            datetime.today().strftime('%H-%M-%S'),
            request.path,
            request.method,
        )})
        logging.error({"дата: {}, время: {}, запрошенный URL: {}, HTTP метод: {}".format(
            datetime.today().strftime('%d-%m-%Y'),
            datetime.today().strftime('%H-%M-%S'),
            request.path,
            request.method,

        )})
        response = self.get_response(request)
        return response