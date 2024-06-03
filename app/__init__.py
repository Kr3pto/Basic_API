from flask import Flask

app = Flask(__name__)

from app.controllers import *

if __name__ == "__main__":
    app.run()
