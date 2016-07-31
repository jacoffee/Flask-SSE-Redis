# coding=utf-8

from flask import Flask, render_template, json
from flask_sse import sse

app = Flask(__name__)
# 添加Redis服务器地址
app.config['REDIS_URL'] = "redis://127.0.0.1"
# 注册蓝图sse, 并且定义该模块的URL前缀;
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notifications')
def fetch_updates():
    """
         该步骤实际上是向redis的sse频道(channel), 发布了一条消息, 而且是以SSE格式发送的
         即 data: "", 而type则是event-type(前端需要为该事件添加监听器, 以接受数据)
         publish ---> self.redis.publish(channel=channel)
    """
    sse.publish({
        'question': 'which programming is the best?',
        'value': 'Absolutely, PHP',
        'who': 'allen'
    }, type='new_answers')
    return json.dumps({"state": "ok"})

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 400

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)