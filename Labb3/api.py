from flask import Flask, request
from travel_time import *
app = Flask(__name__)


@app.route('/travel_time', methods=["GET"])
def travel_time():
    y_pred = predict(list(dict(request.form).values()))
    return str(y_pred[0])

if __name__ == '__main__':
    app.run()