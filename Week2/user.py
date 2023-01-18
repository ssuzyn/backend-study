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