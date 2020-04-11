from flask import Flask
from data import db_session
from data.users import *
from data.news import *
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/jobs')
def main():
    db_session.global_init('db/blogs.sqlite')
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    users = session.query(User).all()
    return render_template('jobs.html', jobs=jobs, users=users)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
