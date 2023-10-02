from flask import Flask, render_template, request, redirect, url_for, session, flash
import psycopg2
from psycopg2 import sql
import os
chhattisgarh_cities=['Raipur','Durg','bhilai']
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Function to establish a database connection
def connect_db():
    return psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='root',
        host='localhost'
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact-us.html')

# Routes for registration and login
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Your registration route code remains the same
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']  # Retrieve the selected city
        product_url = request.form['product_url']

        conn = connect_db()
        cur = conn.cursor()

        # Insert the request data into the temp_data table, including the city
        insert_query = "INSERT INTO temp_data (Name, city, product_url) VALUES (%s, %s, %s)"
        cur.execute(insert_query, (name, city, product_url))
        conn.commit()

        cur.close()
        conn.close()

        flash('Request submitted successfully!', 'success')
        return redirect(url_for('request_page'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Your login route code remains the same
        # ...

        return redirect(url_for('dashboard'))

    return render_template('login.html')  # Use "login.html" template

@app.route('/submit_request', methods=['POST'])
def submit_request():
    if request.method == 'POST':
        # Your request submission route code remains the same
        # ...if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']  # Retrieve the selected city
        product_url = request.form['product_url']

        conn = connect_db()
        cur = conn.cursor()

        # Insert the request data into the temp_data table, including the city
        insert_query = "INSERT INTO temp_data (Name, city, product_url) VALUES (%s, %s, %s)"
        cur.execute(insert_query, (name, city, product_url))
        conn.commit()

        cur.close()
        conn.close()

        flash('Request submitted successfully!', 'success')
        return redirect(url_for('request_page'))

        

    return render_template('request.html', chhattisgarh_cities=chhattisgarh_cities)

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return "Welcome to the dashboard!"
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
