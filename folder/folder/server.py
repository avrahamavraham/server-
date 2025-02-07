from flask import Flask, render_template, request, jsonify, session
import json
import os
from waitress import serve
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for session management

# Ensure data directory exists
os.makedirs('data', exist_ok=True)
PLAYER_DATA_FILE = 'data/playerdata.json'
USER_DATA_FILE = 'data/userpassword.json'

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

def ensure_admin_exists():
    try:
        with open(USER_DATA_FILE, 'r', encoding='utf-8') as f:
            users_data = json.load(f)
    except FileNotFoundError:
        users_data = {'users': []}

    # Remove any existing admin user
    users_data['users'] = [user for user in users_data['users'] if user['username'] != 'admin']
    
    # Add admin user with password '123'
    admin_password = generate_password_hash('123')
    users_data['users'].append({
        'username': 'admin',
        'password': admin_password
    })

    with open(USER_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(users_data, f, ensure_ascii=False, indent=4)

# Call this when the server starts
ensure_admin_exists()

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

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'חסרים שם משתמש או סיסמה'}), 400

    # Don't allow registration of admin username
    if username.lower() == 'admin':
        return jsonify({'message': 'שם משתמש זה שמור למערכת'}), 400

    try:
        with open(USER_DATA_FILE, 'r', encoding='utf-8') as f:
            users_data = json.load(f)
    except FileNotFoundError:
        users_data = {'users': []}

    # Check if username already exists
    if any(user['username'] == username for user in users_data['users']):
        return jsonify({'message': 'שם המשתמש כבר קיים במערכת'}), 400

    # Hash the password and store the new user
    hashed_password = generate_password_hash(password)
    users_data['users'].append({
        'username': username,
        'password': hashed_password
    })

    with open(USER_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(users_data, f, ensure_ascii=False, indent=4)

    return jsonify({'message': 'ההרשמה בוצעה בהצלחה'}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'חסרים שם משתמש או סיסמה'}), 400

    try:
        with open(USER_DATA_FILE, 'r', encoding='utf-8') as f:
            users_data = json.load(f)
    except FileNotFoundError:
        return jsonify({'message': 'שגיאה במערכת'}), 500

    # Find user and verify password
    user = next((user for user in users_data['users'] if user['username'] == username), None)
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
@app.route('/')
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
    app.run(host="0.0.0.0", port=8000, debug=True)
