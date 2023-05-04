from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbase.db'
db = SQLAlchemy(app)


class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_column = db.Column(db.String(50), nullable=False)
    float_column = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Table %r>' % self.id

@app.route('/')
def start_page():
     return f'main page'

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        txt = request.form['text']
        num = request.form['num']

        new_inf = Table(text_column=txt, float_column=num)
        try:
            db.session.add(new_inf)
            db.session.commit()
            return redirect('/')
        except:
            return "error"
    else:
        return render_template('create.html')

@app.route('/pathwithsml/<string:wrd>/<int:nmbr>')
def nmbr_and_smbls(wrd,nmbr):
     return f'path with {wrd} and {nmbr}'

@app.route('/about')
def about():
     return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

