import flask

app = flask.Flask("pideploy")
app.secret_key = 'hahaidiotverysecurepasswordlol'

@app.route("/")
def main():
    return flask.render_template("login.html")

@app.route("/piapi/main", methods=['POST'])
def apiLogin():
    if flask.request.form['user'] == "admin":
        if flask.request.form['password'] == "admin":
            return flask.render_template("dashboard.html", user="admin")

app.run()