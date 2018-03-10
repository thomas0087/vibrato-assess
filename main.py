import time
import redis
from flask import Flask

cache = redis.Redis(host = 'redis')
app = Flask(__name__)

def get_previous_access():
    return cache.getset('previous_access', time.time())

@app.route('/')
def root_method():
    previous_access = get_previous_access()
    returned_string = "This is a boring method"
    if previous_access:
        seconds_since = int(time.time() - float(previous_access))
        returned_string = f"Still boring and hasn't changed since you asked {seconds_since} seconds ago."
    return returned_string

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
