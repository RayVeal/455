from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


class OverrideForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    course = StringField('What subject is your course (ex. cmsc)?', validators=[DataRequired()])
    course_no = StringField('What is the course number (ex. 455)?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    course = None
    course_no = None
    form = OverrideForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        course = form.course.data
        form.course.data = ''
        course_no = form.course_no.data
        form.course_no.data = ''
    return render_template('index.html', form=form, name=name, course=course, course_no=course_no)


if __name__ == '__main__':
    app.run(debug=True)
