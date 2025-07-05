import os
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from sqlalchemy import create_engine, text


app = Flask(__name__)
metrics = PrometheusMetrics(app)

db_url = f'sqlite:///{os.path.dirname(__file__)}/updater.db'
engine = create_engine(db_url, connect_args={'check_same_thread': False}, echo=True)



@app.route('/')
def main():
    return 'Hello!'


@app.route("/health")
def health():
    resp = jsonify({"status": "healthy"})
    resp.status_code = 200
    return resp


def select_all(_engine, table: str):
    with _engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM {table}"))
        for row in result:
            print(row)


if __name__ == '__main__':
    select_all(engine, 'issues')
    app.run(debug=True)
