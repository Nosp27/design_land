import waitress
import flask

app = flask.Flask(__name__, static_url_path="/static", static_folder="static")


@app.route("/")
def index():
    return flask.render_template("index.html")


if __name__ == '__main__':
    waitress.serve(app)
