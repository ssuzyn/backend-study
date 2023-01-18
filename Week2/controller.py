from flask import request, session
from flask import jsonify, render_template, make_response, redirect
import db, jwt, json
from user import user

def main():
    return "hello week2 !!"

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

def jwtLogin():
    if request.method == 'POST':
        param = request.get_json()
        email = param['email']
        pwd = param['password']
        token = user.loginJWT(email, pwd)
        if token:
            return {"Authorization" : token}, 200
        return jsonify(result=401)

def jwtVerify():
    if request.method == 'POST':
        token = request.headers.get('authorization')
        print(token)
        decode = jwt.decode(token, "secret", 'HS256')
        return decode['email']

def sessionLogin():
    if request.method == 'POST':
        param = request.get_json()
        email = param['email']
        pwd = param['password']
        ss = user.loginSession(email, pwd)
        if ss:
            print(request.cookies)
            return make_response('Login Complete!!')
        return jsonify(result=401)
    else:
        print(request.cookies)
        #print(request.headers['set-cookie'])
        db.database().saveSession(request.cookies['session'], session)
        return "session Login Page"

def sessionVerify():
    if request.method == 'POST':
        param = request.get_json()
        email = param['email']
        print(session)
        if email in session['data']:
            return email
        else: return jsonify(result=401)