# Flask-SSE-Redis
Simple server-push demo built on Flask-SSE-Redis

For this demo to work, please make sure:

+  Redis is installed and started
+  Install flask-sse with `pip install flask_sse`, repo for this package [flask-see](https://github.com/singingwolfboy/flask-sse)

run **`sse_with_redis.py`**, access `http://localhost:5000/` then `http://localhost:5000/notifications` and you will see the changes on the page.
