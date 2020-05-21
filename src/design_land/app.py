import json

import waitress
import flask

app = flask.Flask(__name__, static_url_path="/static", static_folder="static")


@app.route("/sclo")
def index():
    return flask.render_template("index.html", clothes=form_clothes_dict())


def form_clothes_dict():
    with open(app.static_folder + '/item_category_config.json') as config:
        return json.loads(config.read())


if __name__ == '__main__':
    waitress.serve(app)
