from flask import Flask
from server import tournament, tournament_root


app = Flask(__name__)

@app.route('/')
def get_mvp():

    mvps = [str(mvp) for mvp in tournament.pop(tournament_root, 5)]
    return {
        'mvps': mvps
    }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
