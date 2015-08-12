#!/usr/bin/python

import sys
import json
import urllib2
from pprint import pprint
import collections
import time

params1 = collections.OrderedDict([
          ("method", "getAvailableApiList"),
          ("params", []),
          ("id", 1),
          ("version", "1.0")])

params2 = collections.OrderedDict([
          ("method", "startRecMode"),
          ("params", []),
          ("id", 1),
          ("version", "1.0")])

params3 = collections.OrderedDict([
          ("method", "setShootMode"),
          ("params", ["movie"]),
          ("id", 1),
          ("version", "1.0")])

params4 = collections.OrderedDict([
          ("method", "actTakePicture"),
          ("params", []),
          ("id", 1),
          ("version", "1.0")])

def int_or_str(v):
    if v.lower() == "false":
        return False
    if v.lower() == "true":
        return True

    try:
        return int(v)
    except ValueError:
        return v

if len(sys.argv) > 1:
    params["method"] = sys.argv[1]
    if len(sys.argv) > 2:
        params["params"] = [int_or_str(v) for v in sys.argv[2:]]

print urllib2.urlopen("http://192.168.122.1:8080/sony/camera",
    json.dumps(params1)).read()
print urllib2.urlopen("http://192.168.122.1:8080/sony/camera",
    json.dumps(params2)).read()
time.sleep(5)
# print urllib2.urlopen("http://192.168.122.1:8080/sony/camera",
#     json.dumps(params3)).read()
print urllib2.urlopen("http://192.168.122.1:8080/sony/camera",
    json.dumps(params4)).read()