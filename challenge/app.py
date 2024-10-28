import os
from flask import Flask, render_template 
import redis

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', redis)
redis_port = os.getenv('REDIS_PORT', 6379)

db = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
db.set("counter", 0)

@app.route('/')
def Welcome():
    return render_template('index.html')


@app.route('/counter')
def Visitcounter():
    db.incr("counter")
    counter_value = db.get("counter")
    return render_template('visitcounter.html', counter=counter_value)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
