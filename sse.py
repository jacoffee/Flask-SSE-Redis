# coding=utf-8

# [flask structure](http://flask.pocoo.org/docs/0.11/patterns/packages/)
import itertools
import time
from flask import Flask, Response

app = Flask(__name__)

# app.add_url_rule("/", endpoint="index", view_func=index)
@app.route("/")
def index():
    def generator():
        for num in itertools.cycle('123456'):
            yield "data: %s \n" % num
            time.sleep(0.5)
    # 注意响应头中的content_type
    return Response(generator(), content_type='text/event-stream')

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)

