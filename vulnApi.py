from flask import Flask

app = Flask(__name__)


@app.route('/api/secret')
def secret():
    return 'Secret that no one can know: The admin can be easily bribed with schocolate cake!'
