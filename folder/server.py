from flask import Flask, render_template,request
from waitress import serve
app = Flask(__name__)
@app.route('/')
@app.route('/statt new')
def statt_new():
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
@app.route('/')
@app.route('/cards')
def cards():
    return render_template(
        "cards.html"
    )
@app.route('/')
@app.route('/game')
def game():
    return render_template(
        "game.html"
    )
@app.route('/')
@app.route('/hnot')
def hnot():
    return render_template(
        "hnot.html"
    )
@app.route('/')
@app.route('/index')
def index():
    return render_template(
        "index.html"
    )
@app.route('/')
@app.route('/isof')
def isof():
    return render_template(
        "isof.html"
    )
@app.route('/')
@app.route('/map')
def map():
    return render_template(
        "map.html"
    )
@app.route('/')
@app.route('/personal-areahtml')
def personal_areahtml():
    return render_template(
        "personal-area.html"
    )
@app.route('/')
@app.route('/personalareatxt')
def personal_areatxt():
    return render_template(
        "personal-area.txt"
    )
@app.route('/')
@app.route('/shimosh')
def shimosh():
    return render_template(
        "shimosh.html"
    )
@app.route('/')
@app.route('/timeh')
def timeh():
    return render_template(
        "timeh.html"
    )
@app.route('/')
@app.route('/דוקרבבןשחקנים')
def דוקרבבןשחקנים():
    return render_template(
        "דו קרב בין שחקנים.html"
    )
@app.route('/')
@app.route('/דו קרב מחשב')
def דוקרבמחשב():
    return render_template(
        "דו קרב מחשב.html"
    )
if __name__ == "__main__" :
    serve(app,host="0.0.0.0",port = 8000)
