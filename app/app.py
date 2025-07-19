from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Хост Redis берём из переменной окружения
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_client = redis.Redis(host=redis_host, port=6379, db=0)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok"})

@app.route('/count', methods=['GET'])
def count():
    count = redis_client.incr("counter")
    return jsonify({"visits": count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# TODO: health‑check endpoint
