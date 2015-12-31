from flask import Flask
import cache

app = Flask(__name__)
app.host = "127.0.0.1"
app.port = "5000"
app.register_module(cache.cache, url_prefix='/cache')


if __name__ == "__main__":
    app.run(debug=True)
