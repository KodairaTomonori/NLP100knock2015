from bottle import route, run


@route('/hello')
def hello():
    raw_input()
    return "herrou"


run(host = 'localhost', port = 8080, debug = True, reloader = True)
