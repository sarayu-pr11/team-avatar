from flask import Blueprint, render_template
from algorithm.image import image_data

starter_bp = Blueprint('starter', __name__,
                       url_prefix='/starter',
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='assets')


@app.route('/rgb2/')
def rgb2():
    return render_template('static/rgb_sarayu.html', images=image_data())