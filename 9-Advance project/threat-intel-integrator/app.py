from flask import Flask, render_template, request
import sqlite3
import main 

app = Flask(__name__)

# Helper function to connect to our new SQLite database
def get_db_connection():
    conn = sqlite3.connect('threats.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    scan_result = None
    target_ioc = None
    
    if request.method == 'POST':
        target_ioc = request.form.get('ioc_input')
        ioc_type_id = request.form.get('ioc_type')
        
        # Convert the dropdown ID back to a readable string for the database
        type_mapping = {'1': 'IP', '2': 'Domain', '3': 'Hash'}
        ioc_type_str = type_mapping.get(ioc_type_id, 'Unknown')
        
        if target_ioc and ioc_type_id:
            scan_result = main.scan_ioc(target_ioc, ioc_type_id)
            
            # NEW: Save the results permanently into the database!
            if scan_result:
                conn = get_db_connection()
                conn.execute('INSERT INTO scans (ioc, ioc_type, malicious, suspicious, harmless) VALUES (?, ?, ?, ?, ?)',
                             (scan_result['IOC'], ioc_type_str, scan_result['Malicious'], scan_result['Suspicious'], scan_result['Harmless']))
                conn.commit()
                conn.close()

    # NEW: Fetch the 5 most recent scans from the database to display on the webpage
    conn = get_db_connection()
    recent_scans = conn.execute('SELECT * FROM scans ORDER BY timestamp DESC LIMIT 5').fetchall()
    conn.close()
            
    return render_template('index.html', result=scan_result, target=target_ioc, history=recent_scans)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
