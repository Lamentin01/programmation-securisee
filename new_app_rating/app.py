#!/usr/bin/env python3
"""use_of_templates/app.py
Develop the power of Flask and Jinja by creating HTML templates,
expending those templates, and pass variable to create dynamic content.
"""

import datetime  # import a library to manage dates

import flask  # import the flask library

app = flask.Flask(__name__)  # instantiate a minimal webserver


@app.route('/')  # create the index route
def index():
    # we moved the HTML inside the 'templates/' directory
    # the documentation for the template engine is available here:
    # https://jinja.palletsprojects.com/

    return flask.render_template('index.html')


@app.route('/time/')  # create a new route
def time():
    now = datetime.datetime.now()
    date = now.strftime('%d/%m/%Y')
    hour = now.strftime('%H:%M')

    # we can pass some data to the template to create dynamic content
    # to create variables inside the template, use keywords arguments with
    # name=value
    return flask.render_template('time.html', date=date, hour=hour)


# create a new route to show the results
@app.route('/show/', methods=['POST'])
def show():
    subject = flask.request.form['subject']
    rate = flask.request.form['rate']
    return flask.render_template('show.html', subject=subject, rate=rate)


# create a new route to rating different subjects
@app.route('/rating/', methods=['POST', 'GET'])
def rating():
    return flask.render_template('rating.html')


if __name__ == '__main__':  # consider this line as the main
    # start web server in debug mode on port 8080
    app.run('0.0.0.0', 8080, debug=True)
