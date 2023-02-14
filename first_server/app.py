#!/usr/bin/env python3
"""first_server/app.py
Present a minimal web server with the Flask framework.
Use it as a starting point for your project.
"""


import flask  # import the flask library

app = flask.Flask(__name__)  # instantiate a minimal webserver

# write some HTML
index_page = '''
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <title>First server in Python with Flask</title>
</head>

<body>
  <h1>Welcome on your first web server in Python!</h1>
</body>
</html>
'''


@app.route('/')  # create the index route
def index():
    return index_page, 200  # return HTML with HTTP status code 200


if __name__ == '__main__':  # consider this line as the main
    app.run('0.0.0.0', 8080, debug=True)  # start web server in debug mode on port 8080

app.run(debug=True)