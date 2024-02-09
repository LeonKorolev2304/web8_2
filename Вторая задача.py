from flask import render_template, Flask

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
