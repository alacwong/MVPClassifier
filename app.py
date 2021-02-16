from flask import Flask
from flask import request
from caching import r
from classifier import load_tournament
import pickle

app = Flask(__name__)
load_tournament()


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
        'mvps': mvps
    }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
