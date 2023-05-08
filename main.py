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


@app.route('/rows')
def rows():
    inform = Table.query.order_by(-Table.id).all()
    return render_template('rows.html', inform=inform)


@app.route('/rows/<int:id>')
def row(id):
    inform = Table.query.get(id)
    return render_template('row.html', inform=inform)


@app.route('/rows/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        txt = request.form['text']
        num = request.form['num']

        new_inf = Table(text_column=txt, float_column=num)
        try:
            db.session.add(new_inf)
            db.session.commit()
            return redirect('/rows')
        except:
            return redirect()
    else:
        return render_template('create.html')


@app.route('/rows/<int:id>/delete')
def delete(id):
    inform = Table.query.get_or_404(id)
    try:
        db.session.delete(inform)
        db.session.commit()
        return redirect('/rows')
    except:
        return 'Error'


@app.route('/rows/<int:id>/update', methods=['POST', 'GET'])
def update(id):
    inform = Table.query.get(id)
    if request.method == 'POST':
        inform.text_column = request.form['text']
        inform.float_column = request.form['num']

        try:
            db.session.commit()
            return redirect(f'/rows/{id}')
        except:
            return 'Error'
    else:
        return render_template('update.html', inform=inform)


@app.route('/pathwithsml/<string:wrd>/<int:nmbr>')
def nmbr_and_smbls(wrd,nmbr):
    return f'path with {wrd} and {nmbr}'



@app.route('/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

