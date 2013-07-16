import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

app.config.update(
	DEBUG=True,
)


@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/mfdoom")
def aboutMF():
	return render_template('base.html')


#-------------------
# launch
#-------------------

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='localhost', port=port)