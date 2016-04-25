from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("application-form.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")
@app.route("/application")
def application_feedback():
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    sal = request.args.get("salary")
    job = request.args.get("job")

    return render_template ("application.html", name=firstname, name2=lastname, salary=sal, job=job)

if __name__ == "__main__":
    app.run(debug=True)
