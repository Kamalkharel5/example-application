# import os
# from flask import Flask

# app = Flask(__name__)
# version = os.getenv("APP_VERSION", "unknown")

# @app.route('/')
# def index():
#     return f'Hello Argo CD {version}!'

# app.run(host='0.0.0.0', port=8080)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'v4.0.0 - BROKEN VERSION!'  # Pretend this is broken

app.run(host='0.0.0.0', port=8080)