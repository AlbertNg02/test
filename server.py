from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('client.html')

@socketio.on('connect')
def handle_connect():
    print('A client connected')
    emit('server_event', {'data': 'Hello from server'})  # Emit event from server to client

@socketio.on('disconnect')
def handle_disconnect():
    print('A client disconnected')

@socketio.on('custom_event')
def handle_custom_event(data):
    print('Received custom event from client:', data)

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    print(f"Server running at http://{host}:{port}")
    socketio.run(app, host=host, port=port)
