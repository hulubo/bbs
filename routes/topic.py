from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import *

from models.topic import Topic


main = Blueprint('topic', __name__)


@main.route("/")
def index():
    topics = Topic.all()
    return render_template("topic/index.html", topics=topics)

