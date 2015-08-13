#!/usr/bin/env python

import threading
import os
import time

import CameraServer
import SonyCamera

# JSON web interface server
servaddr = ('0.0.0.0', 9000)
#servaddr = ('127.0.0.1', 9000)
try:
	print("Creating server...")
	cam = SonyCamera.Camera()
	cam.startRecMode()
	time.sleep(2)
	server = CameraServer.ImageServer(servaddr, cam)
	
	server.set_status("Set up camera.")

	#server.set_status(cam.startRecMode())

	
	server.set_status("Starting main loop...")
	#print("Starting Main Loop...")
	while True:
		#server.set_status("Running...")
		if server.is_finished():
			break


except KeyboardInterrupt:
	server.shutdown()
except Exception as ex:
	print(ex)
	server.shutdown()
	#server.set_status(str(ex))