<<<<<<< HEAD
1
=======
#!/usr/bin/python3
"""script that starts a flask application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 20ee44c886a05ea7e03b8a77b6571e8c92eb71b8
