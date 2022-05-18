
from . import main
from flask import redirect, render_template, url_for, request, flash

# view = Blueprint('views', __name__)


@main.route('/')
def index():
  title = 'Welcome to Tours and Travel | Explore your world'

  return render_template('index.html')

