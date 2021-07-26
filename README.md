# flask-api-example

This example project provides a minimal configuration for a `production-ready` Flask API project. It includes a basic project structure and `seed` files for functional and non-function testing, a basic application structure (including error-handling blueprint), and a few assorted `getting started` files too.

The example has been set up for use with Python >= 3.7 and [Docker](https://www.docker.com/). 

## 1.1. Dependencies

* [flask](https://github.com/pallets/flask) v2.x
* [gunicorn](https://github.com/benoitc/gunicorn)

## 1.2. Running locally

`venv` is prefered to run the development locally.

```bash
$ python -m venv venv/flask
$ source ./venv/flask/bin/activate
```

Optional, just type `deactivate` to quit virtual environment.

To run the basic server, you'll need to install a few requirements. To do this, run:

```bash
$ pip install -r requirements/common.txt
```

This will install only the dependencies required to run the server. To boot up the 
default server, you can run:

```bash
$ bash bin/run.sh
```

This will start a [Gunicorn](https://gunicorn.org/) server that wraps the Flask app defined in `src/app.py`. Note that [this is one of the recommended ways of deploying a Flask app 'in production'](https://flask.palletsprojects.com/en/2.0.x/deploying/wsgi-standalone/). The server shipped with Flask is [intended for development purposes only](https://flask.palletsprojects.com/en/2.0.x/deploying/).  

You should now be able to send:

```bash
$ curl localhost:8080/health
```

And receive the response `OK` and status code `200`. 

## 1.3. Running with `docker`

Unsurprisingly, you'll need Docker installed to run this project with Docker. To build a containerised version of the API, run:

```bash
$ docker build . -t flask-app
```

To launch the containerised app, run:

```bash
$ docker run -p 8080:8080 flask-app
```

You should see your server boot up, and should be accessible as before.

## 1.4. Developing with the template

To develop with this example project, install the project's development dependencies. You can do this with:

```bash
pip install -r requirements/develop.txt
```

This'll install some style formatting and testing tools (including `pytest` and `locust`).

* [black](https://github.com/psf/black) - the uncompromising Python code formatter.
* [isort](https://github.com/PyCQA/isort) - a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type. 
* [flake8](https://github.com/PyCQA/flake8) - a python tool that glues together pycodestyle, pyflakes, mccabe, and third-party plugins to check the style and quality of some python code.
* [pytest](https://github.com/pytest-dev/pytest) - The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.
* [locust](https://github.com/locustio/locust) - Scalable user load testing tool written in Python