from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Route to render the contact form page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        state = request.form['state']
        zipcode = request.form['zipcode']
        message = request.form['message']

        # Save form data to SQLite database
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fullname TEXT,
                phone TEXT,
                email TEXT,
                state TEXT,
                zipcode TEXT,
                message TEXT
            )
        ''')
        c.execute('''
            INSERT INTO contacts (fullname, phone, email, state, zipcode, message)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (fullname, phone, email, state, zipcode, message))
        conn.commit()
        conn.close()

        return 'success'  # Return success message to AJAX request

if __name__ == '__main__':
    app.run(debug=True)
