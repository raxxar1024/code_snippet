# coding:utf-8


def simple_app(environ, start_response):
    """    """
    status = "200 OK"
    response_headers = [("Content-type", "text-plain")]
    start_response(status, response_headers)
    return ['Hello world !\n']


class AppClass(object):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plan')]

    def __call__(self, environ, start_response):
        print(environ, start_response)
        start_response(self.status, self.response_headers)
        return ['Hello AppClass.__call__\n']


application = AppClass()
