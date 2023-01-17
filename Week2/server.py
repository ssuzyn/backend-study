from flask import Flask, request, jsonify, render_template, make_response
import db, jwt

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return "hello week2 !!"

@app.route("/v1/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        param = request.get_json()
        email = param['email']
        pwd = param['password']

        if(db.database().overlapEmail(email)):
            return make_response('Already Registerd!')
        else:
            db.database().signup(email, pwd)
            return make_response('Register Complete!!')

@app.route("/v1/login/jwtLogin", methods=["GET", "POST"])
def jwtLogin():
    if request.method == 'POST':
        param = request.get_json()
        email = param['email']
        pwd = param['password']
        info = db.database().login(email, pwd)
        if(info):
            token = jwt.encode(info, "secret", algorithm="HS256")
            print(token)
            return make_response('Login Complete!')


if __name__ == "__main__":
    app.run(debug=True)