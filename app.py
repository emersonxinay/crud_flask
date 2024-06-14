from flask import Flask, request, jsonify, render_template, redirect, url_for
import psycopg2

app = Flask(__name__)

# Conexión a la base de datos
conn = psycopg2.connect(
    host="localhost",
    database="ejemplo",
    user="postgres",
    password="emerson123",
    port="5432"
)

# Creación de tablas
def create_tables():
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        )
    ''')
    conn.commit()
    cur.close()

create_tables()

# Operaciones CRUD
# Obtener datos
@app.route('/')
def index():
    cur = conn.cursor()
    cur.execute('SELECT * FROM items')
    items = cur.fetchall()
    cur.close()
    return render_template('index.html', items=items)

# Para crear un item
@app.route('/items', methods=['POST'])
def create_item():
    name = request.form['name']
    cur = conn.cursor()
    cur.execute('INSERT INTO items (name) VALUES (%s)', (name,))
    conn.commit()
    cur.close()
    return redirect(url_for('index'))

# Para actualizar un item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    new_name = data['name']
    cur = conn.cursor()
    cur.execute('UPDATE items SET name = %s WHERE id = %s', (new_name, item_id))
    conn.commit()
    cur.close()
    return jsonify({'message': 'Item actualizado correctamente'})

@app.route('/update/<int:item_id>', methods=['GET', 'POST'])
def update_view(item_id):
    if request.method == 'POST':
        new_name = request.form['name']
        cur = conn.cursor()
        cur.execute('UPDATE items SET name = %s WHERE id = %s', (new_name, item_id))
        conn.commit()
        cur.close()
        return redirect(url_for('index'))
    else:
        cur = conn.cursor()
        cur.execute('SELECT id, name FROM items WHERE id = %s', (item_id,))
        item = cur.fetchone()
        cur.close()
        return render_template('update.html', item=item)

# Eliminar un item
@app.route('/items/<int:item_id>/delete', methods=['POST'])
def delete_item(item_id):
    cur = conn.cursor()
    cur.execute('DELETE FROM items WHERE id = %s', (item_id,))
    conn.commit()
    cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
