from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
	return render_template('main.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)