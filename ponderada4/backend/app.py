from flask import Flask, render_template, request, redirect, url_for, jsonify
import psycopg2
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required
)

app = Flask(__name__)

# Configuração do JWT
app.config['JWT_SECRET_KEY'] = 'd1aeaaf21ead045668dff72c63b225c0'  # Altere para um valor seguro
jwt = JWTManager(app)

# Configuração do banco de dados
db_host = 'database-pond4.coos2r1g1cz0.us-east-1.rds.amazonaws.com'
db_name = 'postgres'
db_user = 'postgres'
db_password = 'pascolito123'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/grafico')
def grafico():
    return render_template('grafico.html')

def connect_to_db():
    return psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )

@app.route('/login', methods=['POST'])
def login():
    try:
        usuario = request.form.get('usuario')
        senha = request.form.get('password')
        
        conn = connect_to_db()
        cursor = conn.cursor()
        
        # Verificar se o usuário existe no banco de dados
        cursor.execute('SELECT * FROM users WHERE usuario = %s AND senha = %s', (usuario, senha))
        user = cursor.fetchone()
        
        if user:
            # Gera um token JWT
            access_token = create_access_token(identity=usuario)
            return jsonify({'access_token': access_token}), 200
        else:
            return 'Login falhou. Verifique suas credenciais.', 401
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/signup', methods=['POST'])
def signup():
    usuario = request.form.get('usuario')
    password = request.form.get('password')
    
    conn = connect_to_db()
    cursor = conn.cursor()
    
    # Inserir o novo usuário no banco de dados
    cursor.execute('INSERT INTO users (email, password) VALUES (%s, %s)', (usuario, password))
    conn.commit()
    
    return 'Cadastro realizado com sucesso!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
