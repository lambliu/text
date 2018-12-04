from flask import Flask
from flask import render_template
from flask import request



app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    m = request.method
    print(m)
    return render_template('login.html')

if __name__ == '__main__':
    app.run()