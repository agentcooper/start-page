from bottle import route, run, response, request
import things

def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if request.method != 'OPTIONS':
            return fn(*args, **kwargs)

    return _enable_cors

@route('/')
def index():
    return {
        "description": "Exposes Things tasks",
        "available_routes": ["/today"]
    }

@route('/today', method=['OPTIONS', 'GET'])
@enable_cors
def index():
    return {
        "tasks": things.today()
    }

run(host='localhost', port=9001, quiet=True)