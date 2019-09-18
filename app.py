from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template('index.html')

@app.route('/start')
def render_start():
    return render_template('start.html')


if __name__ == '__main__':
    app.run()
