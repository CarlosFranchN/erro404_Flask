from flask import render_template
from . import app


@app.route("/")
def main():
    return render_template("/main/index.html")


@app.route("/errorPag")
def error_page():
    return render_template("/erro/errorPag.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("/erro/errorPag.html"), 404
