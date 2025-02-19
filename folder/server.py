from flask import Flask, render_template, request, jsonify, session
import json
import os
from pymongo import MongoClient
from waitress import serve
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for session management

client = MongoClient('mongodb+srv://avrahamgen:eJXt7AKUDanPNPkl@cluster0.hobhy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['game_database']  # Create/use a database named 'game_database'
players_collection = db['players']  # Collection for player data
users_collection = db['users']    # Collection for user data'

# Helper function to read player data
def read_player_data():
    if os.path.exists(PLAYER_DATA_FILE):
        with open(PLAYER_DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Helper function to write player data
def write_player_data(data, player_name):
    player = {'name': player_name}
    data['player'] = player
    with open(PLAYER_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def ensure_admin_exists():
    # Check if admin exists
    admin_user = users_collection.find_one({'username': 'admin'})
    if admin_user:
        # Update admin password if user exists
        users_collection.update_one(
            {'username': 'admin'},
            {'$set': {'password': generate_password_hash('123')}}
        )
    else:
        # Create new admin user
        users_collection.insert_one({
            'username': 'admin',
            'password': generate_password_hash('123')
        })

# Call this when the server starts
ensure_admin_exists()



@app.route('/api/players', methods=['GET'])
def get_players():
    players = list(players_collection.find({}, {'_id': 0}))  # Exclude MongoDB _id field
    return jsonify(players)


@app.route('/api/players', methods=['POST'])
def save_players():
    data = request.get_json()
    # Remove existing players and insert new data
    players_collection.delete_many({})
    if data:  # Check if data is not empty
        players_collection.insert_many(data)
    return jsonify({"status": "success"})
@app.route('/api/player/<name>', methods=['GET'])
def get_player(name):
    player = players_collection.find_one({'name': name}, {'_id': 0})
    if player:
        return jsonify(player)
    return jsonify({}), 404

@app.route('/api/player/<name>', methods=['POST'])
def update_player(name):
    data = request.get_json()
    data['name'] = name  # Ensure the name matches the URL parameter
    
    # Update or insert the player data
    players_collection.update_one(
        {'name': name},
        {'$set': data},
        upsert=True
    )
    return jsonify({"status": "success"})

def create_new_player(username):
    player_data = {
        'name': username,
        # Add any default player properties here
        'experience': 0,
        'level': 1,
        # Add other default player properties as needed
    }
    players_collection.insert_one(player_data)
    return player_data

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': 'חסרים שם משתמש או סיסמה'}), 400

    if username.lower() == 'admin':
        return jsonify({'message': 'שם משתמש זה שמור למערכת'}), 400

    # Check if username already exists
    if users_collection.find_one({'username': username}):
        return jsonify({'message': 'שם המשתמש כבר קיים במערכת'}), 400

    # Create new user
    users_collection.insert_one({
        'username': username,
        'password': generate_password_hash(password)
    })

    # Create a new player profile for the user
    create_new_player(username)

    return jsonify({'message': 'ההרשמה בוצעה בהצלחה'}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'חסרים שם משתמש או סיסמה'}), 400

    user = users_collection.find_one({'username': username})
    if user and check_password_hash(user['password'], password):
        session['username'] = username
        return jsonify({'message': 'התחברת בהצלחה'}), 200
    
    return jsonify({'message': 'שם משתמש או סיסמה שגויים'}), 401

@app.route('/')
@app.route('/statt new')
def statt_new():
    return render_template(
        "statt new.html"
    )
@app.route('/world_map')
def world_map():
    is_admin = session.get('username') == 'admin'
    return render_template('world_map.html', is_admin=is_admin)
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
    is_admin = session.get('username') == 'admin'
    return render_template('index.html', is_admin=is_admin)
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

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=10000, threads=8)
