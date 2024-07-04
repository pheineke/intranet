from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))


@app.route('/finance')
def finance():
    return render_template('finance.html')


if __name__ == '__main__':
    app.config.update(
        TEMPLATES_AUTO_RELOAD=True
    )
    app.run(debug=True)
