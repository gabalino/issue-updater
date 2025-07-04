from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/')
def main():
    return 'Hello!'


@app.route("/health")
def health():
    resp = jsonify({"status": "healthy"})
    resp.status_code = 200
    return resp


if __name__ == '__main__':
    app.run(debug=True)
