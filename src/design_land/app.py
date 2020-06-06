import json

import waitress
import flask
from flask import request

app = flask.Flask(__name__, static_url_path="/static", static_folder="static")


@app.route("/sclo")
@app.route("/sclo")
def index():
    img_id = int(flask.request.args.get('slide_id', 0))
    imgs = [
        '/static/img/slide/Mask_Group%s.png' % (i if i > 1 else '') for i in range(1,5)
    ]
    return flask.render_template("index.html", slide_img=imgs[img_id], clothes=form_clothes_dict())


@app.route("/daily_task")
def daily():
    return flask.render_template("daily-task.html")


def form_clothes_dict():
    with open(app.static_folder + '/item_category_config.json') as config:
        return json.loads(config.read())


if __name__ == '__main__':
    waitress.serve(app, port=80)
