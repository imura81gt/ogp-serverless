from __future__ import print_function

import sys, os
# get this file's directory independent of where it's run from
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))
import json
import logging
#import urllib
#import urllib2
#from bs4 import BeautifulSoup
#import lxml
import base64
import requests


log = logging.getLogger()
log.setLevel(logging.DEBUG)

def handler(event, context):
    log.debug(type(event))
    log.debug("Received event {}".format(json.dumps(event)))

    url = event.get("url")

    #response = urllib2.urlopen(url)
    #html = response.read()
    #soup = BeautifulSoup(html, "lxml")
    #log.debug(soup)

    #images = soup.find_all('img')
    #log.debug(images)
    #for img in images:
    #    log.debug(img)

    content = requests.get(url).content
    content_b64 = bytes_to_b64(content)

    return '<img border="0" src="' + content_b64 + '" />'



def bytes_to_b64(bytes):
    if bytes[0] == "\xff" and bytes[1] == "\xd8" and bytes[-2] == "\xff" and bytes[-1] == "\xd9":
        imgsrc = "data:image/jpeg;base64,"
    elif bytes[0] == "\x89" and bytes[1] == "\x50" and bytes[2] == "\x4e" and bytes[3] == "\x47":
        imgsrc = "data:image/png;base64,"
    elif bytes[0] == "\x47" and bytes[1] == "\x49" and bytes[2] == "\x46" and bytes[3] == "\x38":
        imgsrc = "data:image/git;base64,"
    elif bytes[0] == "\x42" and bytes[1] == "\x4d":
        imgsrc = "data:image/bmp;base64,"
    else:
        imgsrc = "data:image/unknown;base64,"
    return imgsrc + base64.b64encode(bytes)

