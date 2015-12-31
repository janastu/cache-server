import flask
from flask import Module, make_response
from urlparse import urlparse
from jpegtran import JPEGImage
import os
import requests

cache = Module(__name__, name="cache")
"""Currently works for jpg image only,
client request can provide args in url,
ex: http://test-cache.com/cache?url='image url'&width='int'&height='int'
"""


@cache.route('/', methods=['GET'])
def create_cache():
    """cache the image at the url passed in query params.
    width and height of the thumbnail can be specified in the params.
    return cached image thereafter."""
    if 'width' in flask.request.args:
        width = int(flask.request.args['width'])
    else:
        width = 200

    if 'height' in flask.request.args:
        height = int(flask.request.args['height'])
    else:
        height = 150
    dirn = urlparse(flask.request.args['url']).netloc
    dirn = os.path.join('cache', dirn)  # Store cache under a directory
    f = urlparse(flask.request.args['url']).path.split(
        '/')[-1]  # Name of the file
    fp = os.path.join(dirn, f)
    fp = os.path.abspath(fp)  # Get absolute path of the file

    if(os.path.isdir(dirn)):
        if os.path.isfile(fp):
            """if the image is already cached, serve it"""
            with open(fp, 'r') as f:
                image = f.read()
        else:
            """cache a low res version of the image"""
            image = create_thumbnail(flask.request.args['url'], fp, width,
                                     height)
    else:
        """Create a directory with the hostname"""
        os.makedirs(dirn)
        image = create_thumbnail(flask.request.args['url'], fp, width, height)
    response = make_response()
    response.data = image
    return response


def create_thumbnail(url, fp, width, height):
    blob = requests.get(url).content
    imgResp = requests.get(flask.request.args['url'])
    image = JPEGImage(blob=blob)
    """Check if downscaling image is possible with requested width and
    height.

    """
    if image.width < width:
        width = width/2

    if image.height < height:
        height = height/2

    image.downscale(width, height, 90).save(fp)
    with open(fp, 'r') as f:
        thumbnail = f.read()
    return thumbnail
