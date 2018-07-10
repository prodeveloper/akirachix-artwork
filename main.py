from flask import (Flask,
                   render_template,
                   request,
                   make_response,
                   redirect
                   )
app = Flask('app')


@app.route('/')
def index():
    return render_template("index.html",)


app.run(debug=True, host='0.0.0.0', port=8080)
