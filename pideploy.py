import flask
import threading
import os

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

@app.route("/main/dashboard")
def dashboard():
    if flask.request.args.get('password') == 'admin':
        return flask.render_template("dashboard.html")

def pkgDeploy(pkg):
    os.system("sudo apt install -y " + pkg)

@app.route("/piapi/deploy/pkg/")
def apiDeployPkg():
    package = flask.request.args.get('pkg')
    thcmd = threading.Thread(target=pkgDeploy, args=(package))    
    thcmd.start()
    return flask.redirect("/main/dashboard?password=admin")

app.run()