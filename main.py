# import "packages" from flask
from flask import Flask, render_template, request
from images import image_data, draw_text_in_image,rgb_saathvika

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/binary/')
def binary():
    return render_template("binary.html")


@app.route('/rgbsarayu/')
def rgbsarayu():
    return render_template("rgb_sarayu.html", images=image_data())


@app.route('/rgbsaathvika/')
def rgbsaathvika():
    rgb_saathvika()
    return render_template("rgb_saathvika.html", images=image_data())


@app.route('/home/')
def home():
    return render_template("home.html")

@app.route('/test/')
def test():
    return render_template("test.html")


@app.route('/rgbpranavi/')
def rgbpranavi():
    draw_text_in_image("Team Color's Text")
    return render_template("rgb_pranavi.html", images=image_data())


@app.route('/sarayu/')
def sarayu():
    return render_template("sarayu.html")


@app.route('/sarayu/', methods=['GET', 'POST'])
def sarayu2():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("sarayu.html", name=name)
    # starting and empty input default
    return render_template("sarayu.html", name="World")


@app.route('/saathvika/')
def saathvika():
    return render_template("saathvika.html")


@app.route('/saathvika/', methods=['GET', 'POST'])
def saathvika2():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("saathvika.html", name=name)
    # starting and empty input default
    return render_template("saathvika.html", name="World")


@app.route('/pranavi/')
def pranavi():
    return render_template("pranavi.html")


@app.route('/pranavi/', methods=['GET', 'POST'])
def pranavi2():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("pranavi.html", name=name)
    # starting and empty input default
    return render_template("pranavi.html", name="World")


@app.route('/greet/')
def greet():
    return render_template("greet.html")


@app.route('/greet/', methods=['GET', 'POST'])
def greet2():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", name=name)
    # starting and empty input default
    return render_template("greet.html", name="World")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)