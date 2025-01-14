import sqlite3
from flask import Flask, render_template, redirect, request


# Configure app
app = Flask(__name__)

# Connect Database
def connect_db():
    conn = sqlite3.connect('transaction.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['POST', 'GET'])
def index():
    conn = connect_db()
    cursor = conn.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    conn.close()
    return render_template('index.html', transactions=transactions)

@app.route('/add', methods=['POST', 'GET'])
def add():
    networks = ["Airtel","Mtn", "9mobile", "Glo"]

    if request.method == 'POST':
        conn = connect_db()
        name = request.form.get("name")
        network = request.form.get("network")
        data_or_airtime = request.form.get("d_or_a")
        payment_method = request.form.get("payment_method")
        plan = request.form.get("plan")
        amount = request.form.get("amount")
        remark = request.form.get("remark")
        if not remark:
            remark = "--"

        conn.execute("INSERT INTO transactions (cust_name, network, data_or_airtime, payment_method, plan, amount, remark) VALUES (?,?,?,?,?,?,?)", (name, network, data_or_airtime, payment_method, plan, amount, remark))
        conn.commit()
        conn.close()
        return redirect('/')
    else:
        return render_template('add.html', network=networks)
    
@app.route('/delete', methods=['POST'])
def delete():
    conn = connect_db()
    conn.execute("DELETE FROM transactions WHERE transaction_id=?", (request.form.get("id"),))
    conn.commit()
    conn.close()
    return redirect('/')
    
   
