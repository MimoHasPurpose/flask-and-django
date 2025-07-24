## flask-and-Django

#### flask:

- lightweight framework

#### flask restful_api:

- **REST** : representational state transfer.

- a minimal flask restful api

```
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
def get(self):
return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
app.run(debug=True)
```

#### using url for todo app:

`$ curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT`

#### using requests:

```
from requests import put, get

 put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()
```

---

#### Django

- python web framework

##### Basic commands:


- `mkdir djangotutorial`
- `conda create --name django`
- `conda activate django`
- `conda install django`
- `python -m django --version`
- `django-admin startproject mysite djangotutorial`
- ` python manage.py runserver`
- `python manage.py startapp polls`

- ###### Terminologies:
  - **ASGI:** Asynchronous server gateway interface
  - **WSGI:** Web server gateway interface

  
