from flask import Flask
import controller as con

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main(): return con.main()

@app.route("/v1/register", methods=["GET", "POST"])
def register(): return con.register()

@app.route("/v1/login/jwtLogin", methods=["GET", "POST"])
def jwtLogin(): return con.jwtLogin

@app.route("/v1/login/jwtVerify", methods=["GET", "POST"])
def jwtVerify(): return con.jwtVerify

@app.route("/v1/login/sessionLogin", methods=["GET", "POST"])
def sessionLogin(): return con.sessionLogin

if __name__ == "__main__":
    app.run(debug=True, port=8000)