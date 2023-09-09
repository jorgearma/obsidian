from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
import yara

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)
    respuesta_bot = yara.obtener_respuesta(msg)  # Aquí pasas el mensaje a tu chatbot Yara
    socketio.emit('message', respuesta_bot)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000)
