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
        remark = request.form.get("remark", "--")

        if not (name and network and data_or_airtime and payment_method and plan and amount):
            return redirect("/error_message")

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

@app.route('/error_message')
def error_message():
    return render_template("error-message.html")

@app.route('/search', methods=['POST'])
def search():
    name = request.form.get("name")
    date = request.form.get("date")
    
    # Check if the user did not enter any search value
    if not name and not date:
        return redirect("/error_message")

    # check if the user entered only the name
    if name and not date:
        conn = connect_db()
        cursor = conn.execute("SELECT * FROM transactions WHERE cust_name LIKE ?", ('%' + name + '%',))
        transactions = cursor.fetchall()
        conn.close()
        return render_template('index.html', transactions=transactions)
    
    # check if the user entered only the date
    if date and not name:
        conn = connect_db()
        cursor = conn.execute("SELECT * FROM transactions WHERE date LIKE ?", ('%' + date + '%',))
        transactions = cursor.fetchall()
        conn.close()
        return render_template('index.html', transactions=transactions)
    
    # check if the user entered both the name and the date
    if name and date:
        conn = connect_db()
        cursor = conn.execute("SELECT * FROM transactions WHERE cust_name LIKE ? AND date LIKE ?", ('%' + name + '%', '%' + date + '%',))
        transactions = cursor.fetchall()
        conn.close()
        return render_template('index.html', transactions=transactions)


    
   
