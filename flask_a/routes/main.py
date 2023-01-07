from flask import Blueprint, render_template

main = Blueprint('main', __name__, static_folder='static', template_folder='templates')


@main.route('/')
def index():
    return render_template('app/index.html')

