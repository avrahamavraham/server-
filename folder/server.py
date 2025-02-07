from flask import Flask, render_template, request, jsonify
import json
import os
from flask import Flask, render_template,request
from waitress import serve

app = Flask(__name__)

# Ensure data directory exists
os.makedirs('data', exist_ok=True)
PLAYER_DATA_FILE = 'data/playerdata.json'

# Helper function to read player data
def read_player_data():
    if os.path.exists(PLAYER_DATA_FILE):
        with open(PLAYER_DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Helper function to write player data
def write_player_data(data):
    with open(PLAYER_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/api/players', methods=['GET'])
def get_players():
    return jsonify(read_player_data())

@app.route('/api/players', methods=['POST'])
def save_players():
    data = request.get_json()
    write_player_data(data)
    return jsonify({"status": "success"})

@app.route('/api/player/<name>', methods=['GET'])
def get_player(name):
    players = read_player_data()
    player = next((p for p in players if p.get('name') == name), None)
    if player:
        return jsonify(player)
    return jsonify({}), 404

@app.route('/api/player/<name>', methods=['POST'])
def update_player(name):
    data = request.get_json()
    players = read_player_data()
    
    # Find and update or add the player
    player_index = next((i for i, p in enumerate(players) if p.get('name') == name), None)
    if player_index is not None:
        players[player_index] = data
    else:
        players.append(data)
    
    write_player_data(players)
    return jsonify({"status": "success"})

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
@app.route('/personal-area')
def personal_area():
    return render_template(
        "personal-area.html"
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
    app.run(host="0.0.0.0",port = 8000)
