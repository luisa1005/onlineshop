from flask import Flask, render_template, request
 
 
 
app = Flask(__name__)
 
@app.route('/home', methods= ['GET', 'POST'])
def home():
  
    
  return  render_template ("Version1.html")


@app.route('/kontaktanfragen.html', methods=['GET', 'POST']) 
def Kundensupport():
 
    if request.method == 'POST':
 
        Name = request.form['Name']
 
        Email = request.form['Email']
 
        Betreff = request.form['Betreff']
 
        Nachricht = request.form['Nachricht']
 
        # Debug-Ausgabe
 
        print(f"Name: {Name}, Email: {Email}, Zustand: {Betreff}, Nachricht: {Nachricht}")
 
         
 
        return "Die Daten wurden erfolgreich übermittelt!"
 
     
 
    return render_template('kontaktanfragen.html')
 
 
 
if __name__ == '__main__' :
 
    app.run(debug=True)
