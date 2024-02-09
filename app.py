from flask import Flask
from flask import render_template
from flask.helpers import send_file
import os
import dotenv
from devcerts.install import ensure_certificates_are_installed 


dotenv.load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/taskpane.html")
def taskpane():
    return render_template("taskpane.html")

@app.route("/commands.html")
def commands():
    return render_template("commands.html")

@app.route("/assets/icon-16.png")
def icon16():
    return send_file("./static/assets/icon-16.png",mimetype='image/png')

@app.route("/assets/icon-32.png")
def icon32():
    return send_file("./static/assets/icon-32.png",mimetype='image/png')

@app.route("/assets/icon-64.png")
def icon64():
    return send_file("./static/assets/icon-64.png",mimetype='image/png')

@app.route("/assets/icon-80.png")
def icon128():
    return send_file("./static/assets/icon-80.png",mimetype='image/png')

@app.route("/assets/logo-filled.png")
def iconlogofilled():
    return send_file("./static/assets/logo-filled.png",mimetype='image/png')

@app.route('/favicon.ico')
def favicon():
    return send_file('./static/favicon.ico', mimetype='image/vnd.microsoft.icon')
    
if __name__ == "__main__":
    if os.environ.get("APP_MODE") == "DEV":
        print("Running in DEV mode")
        # Call the function to ensure certificates are installed and valid
        ensure_certificates_are_installed()

        # Assuming the ensure_certificates_are_installed function updates the default paths as needed
        from devcerts.defaults import localhost_certificate_path, localhost_key_path
        ssl_context = (localhost_certificate_path, localhost_key_path)
        
        app.run(debug=True, ssl_context=ssl_context)
    else:
        app.run(debug=True)
