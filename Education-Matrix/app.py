from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'education_matrix_secret_key'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, 'database.db')


# ── Database ──────────────────────────────────────────────────────────────────
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users(
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        name     TEXT    NOT NULL,
        email    TEXT    UNIQUE NOT NULL,
        password TEXT    NOT NULL
    )''')
    conn.commit()
    conn.close()

init_db()


# ── Auth ──────────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    error = None
    if request.method == 'POST':
        name     = request.form['name'].strip()
        email    = request.form['email'].strip()
        password = request.form['password']
        confirm  = request.form['confirm_password']
        if password != confirm:
            error = 'Passwords do not match.'
        else:
            conn = sqlite3.connect(DB_PATH)
            try:
                conn.execute("INSERT INTO users(name,email,password) VALUES(?,?,?)", (name,email,password))
                conn.commit()
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                error = 'Email already registered.'
            finally:
                conn.close()
    return render_template('register.html', error=error)

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        email    = request.form['email'].strip()
        password = request.form['password']
        if email == 'admin@gmail.com' and password == 'admin123':
            conn  = sqlite3.connect(DB_PATH)
            users = conn.execute("SELECT * FROM users").fetchall()
            conn.close()
            return render_template('admin.html', users=users, total_users=len(users))
        conn = sqlite3.connect(DB_PATH)
        user = conn.execute("SELECT * FROM users WHERE email=? AND password=?", (email,password)).fetchone()
        conn.close()
        if user:
            session['user_name']  = user[1]
            session['user_email'] = user[2]
            return redirect(url_for('dashboard'))
        error = 'Invalid email or password.'
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    name  = session.get('user_name',  'Student')
    email = session.get('user_email', '')
    return render_template('dashboard.html', name=name, email=email)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# ── Education Matrix ──────────────────────────────────────────────────────────
@app.route('/edu/')
def edu_home():
    return render_template('edu/index.html')

@app.route('/edu/main')
def edu_main():
    return render_template('edu/main.html')

@app.route('/edu/fe')
def edu_fe():
    return render_template('edu/fe.html')

@app.route('/edu/se')
def edu_se():
    return render_template('edu/se.html')

@app.route('/edu/te')
def edu_te():
    return render_template('edu/te.html')

@app.route('/edu/be')
def edu_be():
    return render_template('edu/be.html')

@app.route('/edu/fe/bxe')
def edu_bxe():
    return render_template('edu/fe_html_files/bxe.html')

@app.route('/edu/fe/ccc')
def edu_ccc():
    return render_template('edu/fe_html_files/ccc.html')

@app.route('/edu/files/FE/<path:filename>')
def edu_files(filename):
    return send_from_directory(os.path.join(BASE_DIR,'static','files','FE'), filename)


if __name__ == '__main__':
    app.run(debug=True)
