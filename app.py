from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/finance')
def finance():
    return render_template('finance.html')


if __name__ == '__main__':
    app.config.update(
        TEMPLATES_AUTO_RELOAD=True
    )
    app.run(debug=True)
