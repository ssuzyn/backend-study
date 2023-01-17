from flask import Flask, request, jsonify, render_template, make_response
import db, jwt, json

app = Flask(__name__)
algorithm = 'HS256'

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

class User():
    def login(email, pwd):
        info = db.database().login(email, pwd) #payload
        print(type(info))
        if(info):
            token = jwt.encode(info, "secret", algorithm)
            print(type(token))
            return token
        return False

@app.route("/v1/login/jwtLogin", methods=["GET", "POST"])
def jwtLogin():
    if request.method == 'POST':
        param = request.get_json()
        email = param['email']
        pwd = param['password']
        token = User.login(email, pwd)
        if token:
            return {"Authorization" : token}, 200
        return jsonify(result=401)


if __name__ == "__main__":
    app.run(debug=True)