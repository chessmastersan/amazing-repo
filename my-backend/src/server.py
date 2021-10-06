from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World!"

@server.route("/ping")
def ping():
    return "{status: ping}"

@server.route("/pong")
def pong():
    return "{status: pong}"

@server.route("/healthz")
def healthz():
    return "{health: ok}"

if __name__ == "__main__":
   server.run(host="0.0.0.0", port=5000)
