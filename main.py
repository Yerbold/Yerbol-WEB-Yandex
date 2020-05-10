from flask import jsonify, Flask, render_template, redirect, request, make_response, session, abort
from data import db_session
import os

from data.records import Records


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    sessiondb = db_session.create_session()
    all_records = sessiondb.query(Records).all()
    return render_template('index.html', all_records=all_records)


@app.route('/add_record', methods=['GET', 'POST'])
def add_record():
    if request.method == 'POST':
        sessiondb = db_session.create_session()
        record = Records()
        record.cookies_per_second = request.form['cookies per second']
        record.cookies_per_click = request.form['cookies per click']
        record.player = request.form['player']
        record.total_amount = request.form['total amount']
        sessiondb.add(record)
        sessiondb.commit()
        return 'Confirmed'
    else:
        return 'No requests yet'

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    db_session.global_init("db/records.sqlite")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
