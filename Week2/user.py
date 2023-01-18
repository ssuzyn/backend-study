from flask import session
import db, jwt

class user():
    def loginJWT(email, pwd):
        info = db.database().login(email, pwd) #payload
        print(type(info))
        if(info):
            token = jwt.encode(info, "secret", 'HS256')
            print(type(token))
            return token
        return False
    
    def loginSession(email, pwd):
        info = db.database().login(email, pwd) #payload
        if(info):
            session['data'] = email
            session.permanent = True
            return True
        return False
