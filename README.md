# cache-server
Jpegtran, Python Flask Cache and image resizing for jpg images

###Requirements
* Python
* pip
* virtualenv

* `pip install -r requirements.txt`
* `python server.py`

###Client requirements
* call the server at endpoint 
* `/cache?url="imageurl"&width="int:default200px"&height="int:default150px"`
* server will return a image binary response - cached if not already
  available in /cache directory at app route

### TO-DO
* write tests
* Server stops when png links or other conditions fail
