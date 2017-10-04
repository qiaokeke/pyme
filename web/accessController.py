from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/getToken")
def getAccToken():
    from service import wechat
    token = wechat.getAccessToken();
    return token

if __name__ == '__main__':
    app.run()
