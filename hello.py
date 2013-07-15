import os
from flask import Flask, render_template

app = Flask(__name__)

app.config.update(
	DEBUG=True,
)


@app.route("/")
def hello():
	return render_template('base.html')


#-------------------
# launch
#-------------------

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='localhost', port=port)