from flask import Flask, render_template, request
 
 
 
app = Flask(__name__)
 
@app.route('/home', methods= ['GET', 'POST'])
def home():
  
    
  return  render_template ("Version1.html")


@app.route('/kontaktanfragen.html', methods=['GET', 'POST']) 
def add_book():
 
    if request.method == 'POST':
 
        title = request.form['title']
 
        price = request.form['price']
 
        condition = request.form['condition']
 
         
 
        # Debug-Ausgabe
 
        print(f"Titel: {title}, Preis: {price}, Zustand: {condition}")
 
         
 
        return "Die Daten wurden erfolgreich übermittelt!"
 
     
 
    return render_template('kontakanfragen.html')
 
 
 
if __name__ == '__main__' :
 
    app.run(debug=True)
