from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Cambia esto en producción

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Aquí podrías validar las credenciales de un usuario
    session['user'] = request.form['username']
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return f"Hola, {session.get('user')}"

if __name__ == '__main__':
    app.run(debug=True)
