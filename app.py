
from flask import Flask, request, redirect, url_for, render_template, flash
import  os, sys
from flask_frozen import Freezer # Added


app=Flask(__name__,template_folder='templates/', static_folder='static')
freezer = Freezer(app) # Added


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/project/')
def project():
    return render_template('project.html')


@app.route('/blog/')
def blog():
    return render_template('blogs.html')




# if __name__ == '__main__':
#     port = os.environ.get("PORT", 5000)
#     app.run(debug=True, host='0.0.0.0', port = port)


# Modified Main
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=5000)

