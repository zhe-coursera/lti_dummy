import os
from flask import Flask
from flask import render_template
from flask_wtf import Form
from wtforms import DecimalField

from pylti.flask import lti

VERSION = '0.0.1'
app = Flask(__name__)
app.config.from_object('config')

class GradeForm(Form):
    grade = DecimalField('grade')

def error(exception=None):
    return render_template('error.html')

@app.route('/is_up', methods=['GET'])
def hello_world(lti=lti):
    """ Indicate the app is working. Provided for debugging purposes.
    """
    return render_template('up.html', lti=lti)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET'])
@app.route('/lti/', methods=['GET', 'POST'])
@lti(request='initial', error=error, app=app)
def index(lti=lti):
    """ initial access page to the lti provider.  This page provides
    authorization for the user.

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    form = GradeForm()
    return render_template('index.html', form=form, lti=lti)
    # return render_template('index.html', lti=lti)


@app.route('/grade', methods=['POST'])
@lti(request='session', error=error, app=app)
def grade(lti=lti):
    """ post grade

    :param lti: the `lti` object from `pylti`
    :return: grade rendered by grade.html template
    """
    form = GradeForm()
    lti.post_grade(form.grade.data)
    return render_template('grade.html', form=form)


def set_debugging():
    """ enable debug logging

    """
    import logging
    import sys

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

set_debugging()

if __name__ == '__main__':
    """
    For if you want to run the flask development server
    directly
    """
    port = int(os.environ.get("FLASK_LTI_PORT", 5000))
    host = os.environ.get("FLASK_LTI_HOST", "localhost")
    app.run(debug=True, host=host, port=port)
