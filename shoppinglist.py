from flask import Flask, render_template, request, jsonify
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/new')
def new_items():
    return render_template('list.html')


@app.route('/addrec', methods = ['POST'])
def addrec():
    if request.method == 'POST':
        try:
            name = request.form['name']
            price = request.form['price']
            with sql.connect('database.db') as con:
                cur = con.cursor()
                cur.execute('INSERT INTO list(name,price)'
                            'VALUES(?,?)', (name, price))
                con.commit()
                msg = 'Record successfully added'
        except:
            con.rollback()
            msg = 'error in insertion operation'
        finally:
            return render_template('result.html', msg = msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect('database.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute('select * from lists')
    rows = cur.fetchall()
    return render_template('shop.html', rows = rows)


if __name__ == '__main__':
    app.run(debug = True)








app.run()
