from flask import Flask
from flask import request
from caching import r
from classifier import load_tournament
import pickle
from scheduler import start_schedule
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
load_tournament()
start_schedule()


@app.route('/')
def get_mvp():
    tournament = pickle.loads(r.get('tournament'))
    root = pickle.loads(r.get('root'))
    k = request.args.get('k')
    if not k:
        k = 1
    else:
        k = int(request.args.get('k'))
    mvps = [str(mvp) for mvp in tournament.pop(root, k)]
    return {
        'mvps': mvps,
        'last_updated': r.get('time').decode('utf-8')
    }


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
