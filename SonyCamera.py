#!/usr/bin/python

import sys
import json
import urllib2
from pprint import pprint
import collections
import time

class Camera:
	def __init__(self):
		self.shoot_mode = False

	def send(self, params):
		"""Open the url of request"""
		return urllib2.urlopen("http://192.168.122.1:8080/sony/camera",
			json.dumps(params)).read()

	def pack(self, type, *params):
		""" Pack the json data for the HTTP request"""
		data = collections.OrderedDict([
        	("method", type),
        	("params", params),
        	("id", 2),
        	("version", "1.0")])
		return data

	def actTakePicture(self):
		"""function to take picture."""
		params = self.pack("actTakePicture")
		result = self.send(params)
		return result

	def startContShooting(self): ## UNTESTED
		"""function to start continuous shooting."""
		params = self.pack("startContShooting")
		result = self.send(params)
		return result

	def stopContShooting(self): ## UNTESTED
		"""function to stop continuous shooting."""
		params = self.pack("stopContShooting")
		result = self.send(params)
		return result

	def setShootMode(self): ## UNTESTED
		"""function to set a value of shooting mode."""
		params = self.pack("setShootMode")
		result = self.send(params)
		return result

	def startRecMode(self):
		"""function to set up camera for shooting function. 
		Some camera models need this API call before starting liveview, 
		capturing still image, recording movie, or accessing all other camera
		shooting functions."""
		params = self.pack("startRecMode")
		result = self.send(params)
		return result

	def startLiveView(self): ## UNTESTED
		"""function to start liveview."""
		params = self.pack("startLiveview")
		result = self.send(params)
		return result

	def stopLiveView(self): ## UNTESTED
		"""function to stop liveview."""
		params = self.pack("stopLiveview")
		result = self.send(params)
		return result

	def getAvailableApiList(self):
		"""function to get the available API names that the server supports at the moment."""
		params = self.pack("getAvailableApiList")
		result = self.send(params)
		return result

	def actZoom(self,direction,action):
		"""function to zoom."""
		params = self.pack("actZoom",direction,action)
		result = self.send(params)
		return result

	def zoomIn(self):
		"""zoom in slightly"""
		return self.actZoom("in","1shot")

	def zoomInFull(self):
		"""zoom in fully"""
		return self.actZoom("in","start")

	def zoomOut(self):
		"""zoom out slightly"""
		return self.actZoom("out","1shot")

	def zoomOutFull(self):
		"""zoom out full"""
		return self.actZoom("out","start")

	def getEvent(self):
		"""function to get event from the server."""
		params = self.pack("getEvent", True)
		result = self.send(params)
		return result

# cam = Camera()
# print "starting shoot mode"
# print cam.startRecMode()

# #print cam.getAvailableApiList()
# #print "taking picture"
# #print cam.actTakePicture()
# #print cam.stopLiveView()
# #print cam.getEvent()
# #print cam.actZoom("in","start")
# cam.zoomInFull()
# print cam.getEvent()
# time.sleep(3)
# print cam.getEvent()
# print cam.actTakePicture()
# print cam.getEvent()
# print cam.actZoom("out","start")
# print cam.getEvent()
# print cam.actTakePicture()
# print cam.getEvent()