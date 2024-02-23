from flask import render_template, Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/distribution')
def list_humans():
    humans = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('humans.html', humans=humans)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
