from flask import Flask, render_template, request
 
 
 
app = Flask(__name__)
 
@app.route('/home', methods= ['GET', 'POST'])
def home():
  
    
  return  render_template ("Version1.html")

 @app.route('/add_book', methods=['GET', 'POST'])
 
def add_book():
 
    if request.method == 'POST':
 
        title = request.form['title']
 
        price = request.form['price']
 
        condition = request.form['condition']
 
         
 
        # Debug-Ausgabe
 
        print(f"Titel: {title}, Preis: {price}, Zustand: {condition}")
 
         
 
        return "Die Daten wurden erfolgreich übermittelt!"
 
     
 
    return render_template('addbooks.html')
 
 
 
if __name__ == '__main__' :
 
    app.run(debug=True)


import sqlite3
 
 
 
@app.route('/add_book', methods=['GET', 'POST'])
 
def add_book():
 
    if request.method == 'POST':
 
        title = request.form['title']
 
        price = request.form['price']
 
        condition = request.form['condition']
 
         
 
        # Verbindung zur Datenbank herstellen
 
        conn = sqlite3.connect('database.db')
 
        cursor = conn.cursor()
 
         
 
        # Daten einfügen
 
        cursor.execute(f"INSERT INTO books (title, price, condition) VALUES ({title}, {price}, {condition})")
 
         
 
        conn.commit()  
 
        conn.close()  
 
         
 
        return "Das Buch wurde erfolgreich hinzugefügt!"
 
     
 
    return render_template('addbooks.html')
 
if __name__ == '__main__':  
 
    app.run(debug=True)  