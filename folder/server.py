from flask import Flask, render_template,request
from waitress import serve
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template(
        "statt new.html"
    )
@app.route('/')
@app.route('/world_map')
def world_map():
    return render_template(
        "world_map.html"
    )
@app.route('/')
@app.route('/biet_m')
def beit_m():
    return render_template(
        "beit_m.html"
    )
if __name__ == "__main__" :
    app.run(host="0.0.0.0",port = 8000)
