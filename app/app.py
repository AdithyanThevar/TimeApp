from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_time():
    return jsonify({
        "ip": request.headers.get('X-Forwarded-For', request.remote_addr),
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
