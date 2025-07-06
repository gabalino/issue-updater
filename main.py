import os
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from sqlalchemy import create_engine, text


app = Flask('issue-updater')
metrics = PrometheusMetrics(app)

db_url = f'sqlite:///{os.path.dirname(__file__)}/updater.db'
engine = create_engine(db_url, connect_args={'check_same_thread': False}, echo=True)


@app.route('/')
def root():
    return 'Hello!'


@app.route('/favicon.ico')
def favicon():
    return '404'


@app.route("/health")
def health():
    resp = jsonify({"status": "healthy"})
    resp.status_code = 200
    return resp


@app.route('/api/issue', methods=["POST"])
def add_issue() -> list:
    result = []
    if request:
        result = request.json
        print('save to database', result)
    return result


def select_all(_engine, table: str):
    with _engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM {table}"))
        for row in result:
            print(row)


if __name__ == '__main__':
    app.run(debug=True)
