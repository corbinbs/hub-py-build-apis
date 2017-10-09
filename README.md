hubpy API meet up series: Build your own APIs
---------------------------------------------
https://www.meetup.com/hub-py/events/243706336/

During this meet up we discussed the Python WSGI standard and then reviewed/demo'ed
a few frameworks for developing APIs in Python.

Commands
~~~~~~~~

Run the API demo with Flask:
```
FLASK_APP=flask_demo.py flask run -p 8000
```

Run the API demo with Falcon:
```
gunicorn falcon_demo:api -w 3
```

Run the API demo using hug:
```
hug -f hug_demo.py
```

Deploy and run the API demo with Chalice (AWS account info must be set up):
```
cd chalice-demo
chalice deploy
```

Interact with the APIs while running one of the demos:
`GET /hello`
```
http GET localhost:8000/hello
```

`POST /stats`
```
http POST localhost:8000/stats data:=[1,2,3,4,5,6,7,8,9,10] value:=10
```

For Chalice, replace `localhost:8000` with the value printed at the end of the
`chalice deploy` command output.

Related Links
~~~~~~~~~~~~~

PEP 333 -- Python Web Server Gateway Interface v1.0
https://www.python.org/dev/peps/pep-0333/#preface

gunicorn (Green Unicorn) Python WSGI HTTP Server
http://gunicorn.org

Frameworks reviewed and demo'ed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Flask
http://flask.pocoo.org

Falcon
https://falconframework.org

Hug
http://www.hug.rest

Chalice
https://github.com/aws/chalice

Django REST Framework
http://www.django-rest-framework.org

Libraries used within demo apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

boltons: `statsutils`
https://boltons.readthedocs.io/en/latest/statsutils.html

Tools used to demonstrate functionality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HTTPie
https://httpie.org
