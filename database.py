import sqlite3

# Funções do Banco de Dados
def create_connection():
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    return conn, c

def create_table():
    conn, c = create_connection()
    c.execute('''CREATE TABLE IF NOT EXISTS clientes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT,
                  telefone TEXT,
                  email TEXT,
                  endereco TEXT)''')
    conn.commit()
    conn.close()

def add_cliente(nome, telefone, email, endereco):
    conn, c = create_connection()
    c.execute('INSERT INTO clientes (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)',
              (nome, telefone, email, endereco))
    conn.commit()
    conn.close()

def view_all_clientes():
    conn, c = create_connection()
    c.execute('SELECT * FROM clientes')
    data = c.fetchall()
    conn.close()
    return data

def get_cliente_by_id(cliente_id):
    conn, c = create_connection()
    c.execute('SELECT * FROM clientes WHERE id = ?', (cliente_id,))
    data = c.fetchone()
    conn.close()
    return data

def edit_cliente(cliente_id, nome, telefone, email, endereco):
    conn, c = create_connection()
    c.execute('UPDATE clientes SET nome = ?, telefone = ?, email = ?, endereco = ? WHERE id = ?',
              (nome, telefone, email, endereco, cliente_id))
    conn.commit()
    conn.close()

def delete_cliente(cliente_id):
    conn, c = create_connection()
    c.execute('DELETE FROM clientes WHERE id = ?', (cliente_id,))
    conn.commit()
    conn.close()
