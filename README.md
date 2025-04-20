## flask-and-Django

#### flask:

-



#### flask restful_api:

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

