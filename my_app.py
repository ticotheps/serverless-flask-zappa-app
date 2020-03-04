from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world! Welcome to Tico's FIRST-ever serverless microservice! Today's date/time is 03/04/2020 @ 12:28AM.", 200

# We only need this for local development
if __name__ == '__main__':
    app.run()