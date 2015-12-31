# cache-server
Jpegtran, Python Flask Cache and image resizing for jpg images

###Requirements
* Python
* pip
* virtualenv

* `pip install -r requirements.txt`
* `python server.py`

###Client requirements
call the server at endpoint 
`/cache?url="imageurl"&width="int:default200px"&height="int:default150px"`
