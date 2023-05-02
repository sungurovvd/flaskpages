from flask import Flask

app = Flask(__name__)

@app.route('/')
def start_page():
     return f'main page'

@app.route('/pathwithsml/<string:wrd>/<int:nmbr>')
def nmbr_and_smbls(wrd,nmbr):
     return f'path with {wrd} and {nmbr}'


if __name__ == '__main__':
    app.run(debug=True)

