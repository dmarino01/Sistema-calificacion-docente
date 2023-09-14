from flask import Flask, render_template, flash, redirect

from config import config

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    #return redirect(url_for('login'))
    return render_template("home.html")



app.url_map.strict_slashes = False

if __name__ == '__main__':
    app.config.from_object(config['development'])
    #csrf.init_app(app)
    #app.register_error_handler(401,status_401)
    #app.register_error_handler(404,status_404)
    app.run()
