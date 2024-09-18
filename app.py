from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('button_state.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS button_state (id INTEGER PRIMARY KEY, state INTEGER)''')
    c.execute('''INSERT INTO button_state (id, state) SELECT 1, 0 WHERE NOT EXISTS (SELECT 1 FROM button_state WHERE id=1)''')
    conn.commit()
    conn.close()

# Get the current state of the button
def get_button_state():
    conn = sqlite3.connect('button_state.db')
    c = conn.cursor()
    c.execute('SELECT state FROM button_state WHERE id=1')
    state = c.fetchone()[0]
    conn.close()
    return state

# Update the state of the button
def set_button_state(new_state):
    conn = sqlite3.connect('button_state.db')
    c = conn.cursor()
    c.execute('UPDATE button_state SET state=? WHERE id=1', (new_state,))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_button_state', methods=['GET'])
def get_state():
    state = get_button_state()
    return jsonify({'state': state})

@app.route('/toggle_button', methods=['POST'])
def toggle_button():
    state = get_button_state()
    new_state = 1 if state == 0 else 0
    set_button_state(new_state)
    return jsonify({'new_state': new_state})

# if __name__ == '__main__':
#     init_db()
#     app.run(debug=True)
